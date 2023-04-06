import math
from concurrent import futures
from typing import Dict, List, Protocol, runtime_checkable

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

    def __init__(self, *, messaging_client: IMessagingClient) -> None:
        self._messaging_client = messaging_client

    def _create_artifacts(self, *, count: int) -> List[Artifact]:
        configs_by_index = {i: CreateArtifactConfig() for i in range(count)}
        response = self._messaging_client.batch_create_artifact(
            BatchCreateArtifactRequest(configs_by_index=configs_by_index)
        )

        return list(
            map(
                lambda x: ArtifactManager._deserialize_to_artifact(x[1]),
                sorted(response.results_by_index.items(), key=lambda x: x[0]),
            )
        )

    def create_artifact(self, content: bytes) -> ArtifactId:
        artifact_ids = self.create_artifacts([content])
        if len(artifact_ids) != 1:
            raise Exception("expected exactly one artifact to be created")

        return artifact_ids[0]

    def create_artifacts(self, contents: List[bytes]) -> List[ArtifactId]:
        artifacts = self._create_artifacts(count=len(contents))

        configs_by_artifact_id: Dict[str, CreateArtifactPartConfig] = {}
        for i, artifact in enumerate(artifacts):
            content_length = len(contents[i])
            part_count = math.ceil(content_length / artifact.part_size_threshold)

            if part_count == 0:
                # TODO(adrian@preemo.io, 04/05/2023): sort out if there's a reasonable way to handle this case
                raise Exception("artifact contents must not be empty")

            configs_by_artifact_id[artifact.id.value] = CreateArtifactPartConfig(
                metadatas_by_part_number={
                    # TODO(adrian@preemo.io, 04/05/2023): consider if 0-based indexing is more reasonable
                    (1 + j): CreateArtifactPartConfigMetadata()
                    for j in range(part_count)
                }
            )

        response = self._messaging_client.batch_create_artifact_part(
            BatchCreateArtifactPartRequest(
                configs_by_artifact_id=configs_by_artifact_id
            )
        )

        # TODO(adrian@preemo.io, 04/05/2023): pass in max_workers or set as env var
        with futures.ThreadPoolExecutor(max_workers=5) as executor:
            for i, artifact in enumerate(artifacts):
                content = contents[i]

                config = configs_by_artifact_id[artifact.id.value]
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

                    # TODO(adrian@preemo.io, 04/05/2023): okay let's do 0-based lol
                    min_content_index = (part_number - 1) * artifact.part_size_threshold
                    max_content_index = min_content_index + artifact.part_size_threshold

                    metadata.upload_signed_url

                # executor.submit(fn, args)

        # # TODO(adrian@preemo.io, 03/20/2023): should upload in parallel
        # for i, content in enumerate(contents):
        #     artifact_id = artifact_ids[i].value
        #     config = configs_by_artifact_id[artifact_id]
        #     result = response.results_by_artifact_id[artifact_id]

        #     ensure_keys_match(
        #         expected=config.metadatas_by_part_number,
        #         actual=result.metadatas_by_part_number,
        #     )

        #     # TODO(adrian@preemo.io, 03/20/2023): this hard-coded part number will need to change for multi-part upload
        #     metadata = result.metadatas_by_part_number[1]
        #     if not metadata.HasField("upload_signed_url"):
        #         raise Exception("expected result metadata to have upload_signed_url")

        #     # TODO(adrian@preemo.io, 03/20/2023): actually upload to artifact with signed url
        #     # something like upload_content(content, signed_url)

        # self._messaging_client.batch_finalize_artifact(
        #     BatchFinalizeArtifactRequest(
        #         configs_by_artifact_id={
        #             artifact_id.value: FinalizeArtifactConfig()
        #             for artifact_id in artifact_ids
        #         }
        #     )
        # )

        # return artifact_ids

    def get_artifact(self, artifact_id: ArtifactId) -> bytes:
        contents = self.get_artifacts([artifact_id])
        if len(contents) != 1:
            raise Exception("expected exactly one artifact to be retrieved")

        return contents[0]

    def get_artifacts(self, artifact_ids: List[ArtifactId]) -> List[bytes]:
        get_artifact_response = self._messaging_client.batch_get_artifact(
            BatchGetArtifactRequest(
                configs_by_artifact_id={
                    artifact_id.value: GetArtifactConfig()
                    for artifact_id in artifact_ids
                }
            )
        )

        configs_by_artifact_id = {
            artifact_id: GetArtifactPartConfig(
                metadatas_by_part_number={
                    (1 + i): GetArtifactPartConfigMetadata()
                    # TODO(adrian@preemo.io, 03/20/2023): don't necessarily want to attempt to
                    # download the entire artifact all at once
                    for i in range(result.part_count)
                }
            )
            for artifact_id, result in get_artifact_response.results_by_artifact_id.items()
        }
        get_artifact_part_response = self._messaging_client.batch_get_artifact_part(
            BatchGetArtifactPartRequest(configs_by_artifact_id=configs_by_artifact_id)
        )

        results: List[bytes] = []
        for (
            artifact_id,
            result,
        ) in get_artifact_part_response.results_by_artifact_id.items():
            config = configs_by_artifact_id[artifact_id]
            ensure_keys_match(
                expected=config.metadatas_by_part_number,
                actual=result.metadatas_by_part_number,
            )

            # TODO(adrian@preemo.io, 03/20/2023): this hard-coded part number will need to change for multi-part upload
            # metadata = result.metadatas_by_part_number[1]

            # TODO(adrian@preemo.io, 03/20/2023): actually download artifact with signed url
            # something like content = download_content(signed_url)
            # results.append(content)

        return results
