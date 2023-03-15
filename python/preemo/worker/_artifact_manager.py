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


# TODO(adrian@preemo.io, 03/14/2023): use pydantic?
class StringValue:
    def __init__(self, value: str, /) -> None:
        self.value = value


class ArtifactId(StringValue):
    pass


@runtime_checkable
class IArtifactManager(Protocol):
    def create_artifact(self, content: str) -> ArtifactId:
        pass

    # TODO(adrian@preemo.io, 03/14/2023): consider taking and returning map with arbitrary keys?
    def create_artifacts(self, contents: list[str]) -> list[ArtifactId]:
        pass


class ArtifactManager:
    def __init__(self, *, messaging_client: IMessagingClient) -> None:
        self._client = messaging_client

    def _create_artifacts(self, *, count: int) -> list[ArtifactId]:
        configs_by_index = {i: CreateArtifactConfig() for i in range(count)}
        response = self._client.batch_create_artifact(
            BatchCreateArtifactRequest(configs_by_index=configs_by_index)
        )

        # TODO(adrian@preemo.io, 03/14/2023): does this work as expected?
        if response.results_by_index.keys() != configs_by_index.keys():
            raise ValueError(
                "expected results_by_index key set to match configs_by_index key set"
            )

        return list(
            map(
                lambda x: ArtifactId(x[1].artifact_id),
                sorted(response.results_by_index.items(), key=lambda x: x[0]),
            )
        )

    def create_artifact(self, content: str) -> ArtifactId:
        # TODO(adrian@preemo.io, 03/14/2023): implement using batch call
        raise Exception("not yet implemented")

    def create_artifacts(self, contents: list[str]) -> list[ArtifactId]:
        # TODO(adrian@preemo.io, 03/14/2023): handle multipart file upload
        artifact_ids = self._create_artifacts(count=len(contents))

        # TODO(adrian@preemo.io, 03/14/2023): figure out size for creating multiple parts
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

        if response.results_by_artifact_id.keys() != configs_by_artifact_id.keys():
            raise ValueError(
                "expected results_by_artifact_id key set to match configs_by_artifact_id key set"
            )

        # TODO(adrian@preemo.io, 03/14/2023): should upload in parallel
        for i, content in enumerate(contents):
            artifact_id = artifact_ids[i].value
            config = configs_by_artifact_id[artifact_id]
            result = response.results_by_artifact_id[artifact_id]

            if (
                result.metadatas_by_part_number.keys()
                != config.metadatas_by_part_number.keys()
            ):
                raise ValueError(
                    "expected result metadatas_by_part_number key set to match config metadatas_by_part_number key set"
                )

            # TODO(adrian@preemo.io, 03/14/2023): should work for multi-part:
            metadata = result.metadatas_by_part_number[1]
            if not metadata.HasField("upload_signed_url"):
                raise ValueError("expected result metadata to have upload_signed_url")

            # TODO(adrian@preemo.io, 03/14/2023): actually upload to artifact with signed url
            # upload_content(content, signed_url)

        # TODO(adrian@preemo.io, 03/14/2023): batch finalize artifacts

        return artifact_ids


# TODO(adrian@preemo.io, 03/14/2023): do we want/need this?
# This class is intended to be used for tests and local development
class LocalArtifactManager:
    def create_artifact(self, content: str) -> ArtifactId:
        # TODO(adrian@preemo.io, 03/14/2023): print something?
        raise Exception("not yet implemented")

    def create_artifacts(self, contents: list[str]) -> list[ArtifactId]:
        raise Exception("not yet implemented")


# TODO(adrian@preemo.io, 03/14/2023): add test ensuring that these classes fulfill the protocol
