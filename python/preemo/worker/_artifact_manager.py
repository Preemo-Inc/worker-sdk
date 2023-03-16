from typing import Protocol, runtime_checkable

from preemo.gen.endpoints.batch_create_artifact_part_pb2 import (
    BatchCreateArtifactPartRequest,
    CreateArtifactPartConfig,
    CreateArtifactPartConfigMetadata,
)
from preemo.gen.endpoints.batch_create_artifact_pb2 import (
    BatchCreateArtifactRequest,
    CreateArtifactConfig,
)
from preemo.worker._messaging_client import IMessagingClient
from preemo.worker._types import StringValue
from preemo.worker._validation import ensure_keys_match


class ArtifactId(StringValue):
    pass


@runtime_checkable
class IArtifactManager(Protocol):
    def create_artifact(self, content: str) -> ArtifactId:
        pass

    def create_artifacts(self, contents: list[str]) -> list[ArtifactId]:
        pass

    def get_artifact(self, artifact_id: ArtifactId) -> str:
        pass

    def get_artifacts(self, artifact_ids: list[ArtifactId]) -> list[str]:
        pass


class ArtifactManager:
    def __init__(self, *, messaging_client: IMessagingClient) -> None:
        self._client = messaging_client

    def _create_artifacts(self, *, count: int) -> list[ArtifactId]:
        configs_by_index = {i: CreateArtifactConfig() for i in range(count)}
        response = self._client.batch_create_artifact(
            BatchCreateArtifactRequest(configs_by_index=configs_by_index)
        )

        return list(
            map(
                lambda x: ArtifactId(value=x[1].artifact_id),
                sorted(response.results_by_index.items(), key=lambda x: x[0]),
            )
        )

    def create_artifact(self, content: str) -> ArtifactId:
        artifact_ids = self.create_artifacts([content])
        if len(artifact_ids) != 1:
            raise Exception("expected exactly one artifact to be created")

        return artifact_ids[0]

    def create_artifacts(self, contents: list[str]) -> list[ArtifactId]:
        artifact_ids = self._create_artifacts(count=len(contents))

        # TODO(adrian@preemo.io, 03/20/2023): handle multipart file upload
        # figure out size for creating multiple parts (100MB?)
        # and decide best way to get size of content len() for now, maybe sys.getsizeof at some point?
        configs_by_artifact_id = {
            artifact_id.value: CreateArtifactPartConfig(
                metadatas_by_part_number={1: CreateArtifactPartConfigMetadata()}
            )
            for artifact_id in artifact_ids
        }

        response = self._client.batch_create_artifact_part(
            BatchCreateArtifactPartRequest(
                configs_by_artifact_id=configs_by_artifact_id
            )
        )

        # TODO(adrian@preemo.io, 03/14/2023): should upload in parallel
        for i, content in enumerate(contents):
            artifact_id = artifact_ids[i].value
            config = configs_by_artifact_id[artifact_id]
            result = response.results_by_artifact_id[artifact_id]

            ensure_keys_match(
                expected=config.metadatas_by_part_number,
                actual=result.metadatas_by_part_number,
            )

            # TODO(adrian@preemo.io, 03/14/2023): will need to change for multi-part upload
            metadata = result.metadatas_by_part_number[1]
            if not metadata.HasField("upload_signed_url"):
                raise Exception("expected result metadata to have upload_signed_url")

            # TODO(adrian@preemo.io, 03/14/2023): actually upload to artifact with signed url
            # upload_content(content, signed_url)

        # TODO(adrian@preemo.io, 03/14/2023): batch finalize artifacts

        return artifact_ids

    def get_artifact(self, artifact_id: ArtifactId) -> str:
        contents = self.get_artifacts([artifact_id])
        if len(contents) != 1:
            raise Exception("expected exactly one artifact to be retrieved")

        return contents[0]

    def get_artifacts(self, artifact_ids: list[ArtifactId]) -> list[str]:
        # TODO(adrian@preemo.io, 03/15/2023): implement
        raise Exception("not yet implemented")
