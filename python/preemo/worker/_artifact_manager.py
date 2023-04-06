import concurrent.futures
import math
from typing import Dict, List, Protocol, runtime_checkable

import requests
from pydantic import StrictInt

from preemo.gen.endpoints.batch_create_artifact_part_pb2 import (
    BatchCreateArtifactPartRequest,
    CreateArtifactPartConfig,
    CreateArtifactPartConfigMetadata,
)
from preemo.gen.endpoints.batch_create_artifact_pb2 import (
    BatchCreateArtifactRequest,
    CreateArtifactConfig,
    CreateArtifactResult,
)
from preemo.gen.endpoints.batch_finalize_artifact_pb2 import (
    BatchFinalizeArtifactRequest,
    FinalizeArtifactConfig,
)
from preemo.gen.endpoints.batch_get_artifact_part_pb2 import (
    BatchGetArtifactPartRequest,
    GetArtifactPartConfig,
    GetArtifactPartConfigMetadata,
)
from preemo.gen.endpoints.batch_get_artifact_pb2 import (
    BatchGetArtifactRequest,
    GetArtifactConfig,
)
from preemo.worker._messaging_client import IMessagingClient
from preemo.worker._types import ImmutableModel, StringValue
from preemo.worker._validation import ensure_keys_match


class ArtifactId(StringValue):
    pass


class Artifact(ImmutableModel):
    id: ArtifactId
    part_size_threshold: StrictInt


@runtime_checkable
class IArtifactManager(Protocol):
    def create_artifact(self, content: bytes) -> ArtifactId:
        pass

    def create_artifacts(self, contents: List[bytes]) -> List[ArtifactId]:
        pass

    def get_artifact(self, artifact_id: ArtifactId) -> bytes:
        pass

    def get_artifacts(self, artifact_ids: List[ArtifactId]) -> List[bytes]:
        pass


class ArtifactManager:
    @staticmethod
    def _calculate_part_count(*, content_length: int, part_size_threshold: int) -> int:
        return math.ceil(content_length / part_size_threshold)

    @staticmethod
    def _deserialize_to_artifact(result: CreateArtifactResult) -> Artifact:
        if not result.HasField("artifact_id"):
            raise Exception("expected create artifact result to have artifact_id")

        if not result.HasField("part_size_threshold"):
            raise Exception(
                "expected create artifact result to have part_size_threshold"
            )

        return Artifact(
            id=ArtifactId(value=result.artifact_id),
            part_size_threshold=result.part_size_threshold,
        )

    @staticmethod
    def _upload_content(*, content: memoryview, url: str) -> None:
        # TODO(adrian@preemo.io, 04/06/2023): how to force gzip
        response = requests.put(url=url, data=content)

        # TODO(adrian@preemo.io, 04/06/2023): should probably retry
        if not response.ok:
            raise Exception(f"unexpected response while uploading: {response}")

    @staticmethod
    def _download_content(*, url: str) -> bytes:
        # TODO(adrian@preemo.io, 04/06/2023): how to force (un)gzip
        response = requests.get(url=url)

        # TODO(adrian@preemo.io, 04/06/2023): should probably retry
        if not response.ok:
            raise Exception(f"unexpected response while downloading: {response}")

        return response.content

    def __init__(
        self,
        *,
        max_download_threads: int,
        max_upload_threads: int,
        messaging_client: IMessagingClient,
    ) -> None:
        if max_download_threads <= 0:
            raise ValueError("max_download_threads must be positive")

        if max_upload_threads <= 0:
            raise ValueError("max_upload_threads must be positive")

        self._max_download_threads = max_download_threads
        self._max_upload_threads = max_upload_threads
        self._messaging_client = messaging_client

    def _create_artifacts(self, *, count: int) -> List[Artifact]:
        configs_by_index = {i: CreateArtifactConfig() for i in range(count)}
        response = self._messaging_client.batch_create_artifact(
            BatchCreateArtifactRequest(configs_by_index=configs_by_index)
        )

        artifacts = list(
            map(
                lambda x: ArtifactManager._deserialize_to_artifact(x[1]),
                sorted(response.results_by_index.items(), key=lambda x: x[0]),
            )
        )

        if len(artifacts) != count:
            raise Exception("received unexpected artifact count")

        return artifacts

    def create_artifact(self, content: bytes) -> ArtifactId:
        artifact_ids = self.create_artifacts([content])
        if len(artifact_ids) != 1:
            raise Exception("expected exactly one artifact to be created")

        return artifact_ids[0]

    def create_artifacts(self, contents: List[bytes]) -> List[ArtifactId]:
        artifacts = self._create_artifacts(count=len(contents))

        configs_by_artifact_id_value: Dict[str, CreateArtifactPartConfig] = {}
        for artifact, content in zip(artifacts, contents):
            part_count = ArtifactManager._calculate_part_count(
                content_length=len(content),
                part_size_threshold=artifact.part_size_threshold,
            )

            if part_count == 0:
                # TODO(adrian@preemo.io, 04/05/2023): sort out if there's a reasonable way to handle this case
                raise Exception("artifact contents must not be empty")

            configs_by_artifact_id_value[artifact.id.value] = CreateArtifactPartConfig(
                metadatas_by_part_number={
                    part_number: CreateArtifactPartConfigMetadata()
                    for part_number in range(part_count)
                }
            )

        response = self._messaging_client.batch_create_artifact_part(
            BatchCreateArtifactPartRequest(
                configs_by_artifact_id=configs_by_artifact_id_value
            )
        )

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self._max_upload_threads
        ) as executor:
            futures = []
            for artifact, content in zip(artifacts, contents):
                content_view = memoryview(content)

                config = configs_by_artifact_id_value[artifact.id.value]
                result = response.results_by_artifact_id[artifact.id.value]
                ensure_keys_match(
                    expected=config.metadatas_by_part_number,
                    actual=result.metadatas_by_part_number,
                )

                for part_number, metadata in result.metadatas_by_part_number.items():
                    if not metadata.HasField("upload_signed_url"):
                        raise Exception(
                            "expected result metadata to have upload_signed_url"
                        )

                    start_index = part_number * artifact.part_size_threshold
                    part_content = content_view[
                        start_index : start_index + artifact.part_size_threshold
                    ]

                    futures.append(
                        executor.submit(
                            ArtifactManager._upload_content,
                            content=part_content,
                            url=metadata.upload_signed_url,
                        )
                    )

            # TODO(adrian@preemo.io, 04/05/2023): exception handling
            done, not_done = concurrent.futures.wait(
                futures, return_when=concurrent.futures.ALL_COMPLETED
            )

            if len(not_done) != 0:
                raise Exception("expected incomplete future set to be empty")

            if len(done) != len(futures):
                raise Exception("expected all futures to have completed")

        self._messaging_client.batch_finalize_artifact(
            BatchFinalizeArtifactRequest(
                configs_by_artifact_id={
                    artifact.id.value: FinalizeArtifactConfig(
                        total_size=len(content),
                        part_count=ArtifactManager._calculate_part_count(
                            content_length=len(content),
                            part_size_threshold=artifact.part_size_threshold,
                        ),
                    )
                    for artifact, content in zip(artifacts, contents)
                }
            )
        )

        return list(map(lambda a: a.id, artifacts))

    def get_artifact(self, artifact_id: ArtifactId) -> bytes:
        contents = self.get_artifacts([artifact_id])
        if len(contents) != 1:
            raise Exception("expected exactly one artifact to be retrieved")

        return contents[0]

    def get_artifacts(self, artifact_ids: List[ArtifactId]) -> List[bytes]:
        # TODO(adrian@preemo.io, 04/05/2023): fix this whole implementation
        get_artifact_response = self._messaging_client.batch_get_artifact(
            BatchGetArtifactRequest(
                configs_by_artifact_id={
                    artifact_id.value: GetArtifactConfig()
                    for artifact_id in artifact_ids
                }
            )
        )

        configs_by_artifact_id_value = {
            artifact_id_value: GetArtifactPartConfig(
                metadatas_by_part_number={
                    part_number: GetArtifactPartConfigMetadata()
                    for part_number in range(result.part_count)
                }
            )
            for artifact_id_value, result in get_artifact_response.results_by_artifact_id.items()
        }
        get_artifact_part_response = self._messaging_client.batch_get_artifact_part(
            BatchGetArtifactPartRequest(
                configs_by_artifact_id=configs_by_artifact_id_value
            )
        )

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self._max_download_threads
        ) as executor:
            futures_by_artifact_id_and_part_number: Dict[
                ArtifactId, Dict[int, concurrent.futures.Future]
            ] = {}
            for (
                artifact_id_value,
                artifact_part_result,
            ) in get_artifact_part_response.results_by_artifact_id.items():
                config = configs_by_artifact_id_value[artifact_id_value]
                ensure_keys_match(
                    expected=config.metadatas_by_part_number,
                    actual=artifact_part_result.metadatas_by_part_number,
                )

                futures_by_part_number: Dict[int, concurrent.futures.Future] = {}
                for (
                    part_number,
                    metadata,
                ) in artifact_part_result.metadatas_by_part_number.items():
                    # TODO(adrian@preemo.io, 04/06/2023): move these expectations/validations into messaging client
                    if not metadata.HasField("download_signed_url"):
                        raise Exception(
                            "expected result metadata to have download_signed_url"
                        )

                    futures_by_part_number[part_number] = executor.submit(
                        ArtifactManager._download_content,
                        url=metadata.download_signed_url,
                    )

                futures_by_artifact_id_and_part_number[
                    ArtifactId(value=artifact_id_value)
                ] = futures_by_part_number

            futures = [
                future
                for futures_by_part_number in futures_by_artifact_id_and_part_number.values()
                for future in futures_by_part_number.values()
            ]
            done, not_done = concurrent.futures.wait(
                futures,
                return_when=concurrent.futures.ALL_COMPLETED,
            )

            if len(not_done) != 0:
                raise Exception("expected incomplete future set to be empty")

            if len(done) != len(futures):
                raise Exception("expected all futures to have completed")

            results: List[bytes] = []
            for artifact_id in artifact_ids:
                futures_by_part_number = futures_by_artifact_id_and_part_number[
                    artifact_id
                ]

                result = bytearray()
                for part_number, future in sorted(
                    futures_by_part_number.items(), key=lambda x: x[0]
                ):
                    # TODO(adrian@preemo.io, 04/06/2023): include validation regarding part size threshold and total size
                    content = future.result()
                    result.extend(content)

                results.append(result)

        return results
