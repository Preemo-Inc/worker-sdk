from typing import Protocol, runtime_checkable

from preemo.gen.endpoints.batch_create_artifact_pb2 import (
    BatchCreateArtifactRequest,
    CreateArtifactConfig,
)
from preemo.worker._messaging_client import IMessagingClient


@runtime_checkable
class IArtifactManager(Protocol):
    def create_artifact(self, content: str) -> str:
        # TODO(adrian@preemo.io, 03/14/2023): should we make an object to avoid comments like "returns artifact id"
        # returns artifact id
        pass

    # TODO(adrian@preemo.io, 03/14/2023): consider taking and returning map with arbitrary keys?
    def create_artifacts(self, contents: list[str]) -> list[str]:
        # returns artifact ids
        pass


class ArtifactManager:
    def __init__(self, *, messaging_client: IMessagingClient) -> None:
        self._client = messaging_client

    def create_artifact(self, content: str) -> str:
        # TODO(adrian@preemo.io, 03/14/2023): implement using batch call
        raise Exception("not yet implemented")

    def create_artifacts(self, contents: list[str]) -> list[str]:
        # TODO(adrian@preemo.io, 03/14/2023): handle multipart file upload
        contents_by_index = {i: content for i, content in enumerate(contents)}
        configs_by_index = {i: CreateArtifactConfig() for i in contents_by_index.keys()}

        response = self._client.batch_create_artifact(
            BatchCreateArtifactRequest(configs_by_index=configs_by_index)
        )

        if len(response.results_by_index) != len(contents):
            # TODO(adrian@preemo.io, 03/14/2023): is this check redundant with the key match?
            raise ValueError("expected the content count and result count to match")

        # TODO(adrian@preemo.io, 03/14/2023): does this work as expected?
        if response.results_by_index.keys() != configs_by_index.keys():
            raise ValueError(
                "expected results_by_index key set to match configs_by_index key set"
            )

        # TODO(adrian@preemo.io, 03/14/2023): merge params with create artifact result
        # { index: { params: '', artifact_id: '' } }
        things_by_index = {}
        for index, content in contents_by_index.items():
            result = response.results_by_index[index]

            things_by_index[index] = {content: content, result: result}

        # TODO(adrian@preemo.io, 03/14/2023): figure out size for creating multiple parts
        self._client.batch_create_artifact_part(
            BatchCreateArtifactPartRequest(configs_by_artifact_id={})
        )

        # TODO(adrian@preemo.io, 03/14/2023): actually upload to artifact
        # TODO(adrian@preemo.io, 03/14/2023): finalize artifact

        return list(
            map(
                lambda x: x[1].artifact_id,
                sorted(response.results_by_index.items(), key=lambda x: x[0]),
            )
        )


# TODO(adrian@preemo.io, 03/14/2023): do we want/need this?
# This class is intended to be used for tests and local development
class LocalArtifactManager:
    def create_artifact(self, content: str) -> str:
        # TODO(adrian@preemo.io, 03/14/2023): print something?
        raise Exception("not yet implemented")

    def create_artifacts(self, contents: list[str]) -> list[str]:
        raise Exception("not yet implemented")


# TODO(adrian@preemo.io, 03/14/2023): add test ensuring that these classes fulfill the protocol
