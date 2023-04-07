from typing import Protocol, runtime_checkable

import grpc

from preemo import __version__
from preemo.gen.endpoints.batch_create_artifact_part_pb2 import (
    BatchCreateArtifactPartRequest,
    BatchCreateArtifactPartResponse,
)
from preemo.gen.endpoints.batch_create_artifact_pb2 import (
    BatchCreateArtifactRequest,
    BatchCreateArtifactResponse,
)
from preemo.gen.endpoints.batch_execute_function_pb2 import (
    BatchExecuteFunctionRequest,
    BatchExecuteFunctionResponse,
)
from preemo.gen.endpoints.batch_finalize_artifact_pb2 import (
    BatchFinalizeArtifactRequest,
    BatchFinalizeArtifactResponse,
)
from preemo.gen.endpoints.batch_get_artifact_part_pb2 import (
    BatchGetArtifactPartRequest,
    BatchGetArtifactPartResponse,
)
from preemo.gen.endpoints.batch_get_artifact_pb2 import (
    BatchGetArtifactRequest,
    BatchGetArtifactResponse,
)
from preemo.gen.endpoints.check_function_pb2 import (
    CheckFunctionRequest,
    CheckFunctionResponse,
)
from preemo.gen.endpoints.header_pb2 import HeaderRequest, HeaderResponse
from preemo.gen.endpoints.register_function_pb2 import (
    RegisterFunctionRequest,
    RegisterFunctionResponse,
)
from preemo.gen.endpoints.sdk_server_ready_pb2 import (
    SDKServerReadyRequest,
    SDKServerReadyResponse,
)
from preemo.gen.services.worker_pb2_grpc import WorkerServiceStub
from preemo.worker._validation import ensure_keys_match


@runtime_checkable
class IMessagingClient(Protocol):
    def batch_create_artifact(
        self, request: BatchCreateArtifactRequest
    ) -> BatchCreateArtifactResponse:
        pass

    def batch_create_artifact_part(
        self, request: BatchCreateArtifactPartRequest
    ) -> BatchCreateArtifactPartResponse:
        pass

    def batch_execute_function(
        self, request: BatchExecuteFunctionRequest
    ) -> BatchExecuteFunctionResponse:
        pass

    def batch_finalize_artifact(
        self, request: BatchFinalizeArtifactRequest
    ) -> BatchFinalizeArtifactResponse:
        pass

    def batch_get_artifact(
        self, request: BatchGetArtifactRequest
    ) -> BatchGetArtifactResponse:
        pass

    def batch_get_artifact_part(
        self, request: BatchGetArtifactPartRequest
    ) -> BatchGetArtifactPartResponse:
        pass

    def check_function(self, request: CheckFunctionRequest) -> CheckFunctionResponse:
        pass

    def register_function(
        self, request: RegisterFunctionRequest
    ) -> RegisterFunctionResponse:
        pass

    def sdk_server_ready(
        self, request: SDKServerReadyRequest
    ) -> SDKServerReadyResponse:
        pass


class MessagingClient:
    def __init__(self, *, worker_server_url: str) -> None:
        # TODO(adrian@preemo.io, 03/25/2023): investigate whether it makes sense to use secure_channel instead
        self._channel = grpc.insecure_channel(target=worker_server_url)
        self._worker_service = WorkerServiceStub(self._channel)

        self._initiate(HeaderRequest(version=__version__))

    def _initiate(self, request: HeaderRequest) -> HeaderResponse:
        return self._worker_service.Initiate(request)

    def batch_create_artifact(
        self, request: BatchCreateArtifactRequest
    ) -> BatchCreateArtifactResponse:
        response = self._worker_service.BatchCreateArtifact(request)
        ensure_keys_match(
            expected=request.configs_by_index, actual=response.results_by_index
        )

        for result in response.results_by_index.values():
            if not result.HasField("artifact_id"):
                raise Exception("expected CreateArtifactResult to have artifact_id")

            if not result.HasField("part_size_threshold"):
                raise Exception(
                    "expected CreateArtifactResult to have part_size_threshold"
                )

        return response

    def batch_create_artifact_part(
        self, request: BatchCreateArtifactPartRequest
    ) -> BatchCreateArtifactPartResponse:
        response = self._worker_service.BatchCreateArtifactPart(request)
        ensure_keys_match(
            expected=request.configs_by_artifact_id,
            actual=response.results_by_artifact_id,
        )

        for artifact_id, result in response.results_by_artifact_id.items():
            config = request.configs_by_artifact_id[artifact_id]
            ensure_keys_match(
                expected=config.metadatas_by_part_number,
                actual=result.metadatas_by_part_number,
            )

            for metadata in result.metadatas_by_part_number.values():
                if not metadata.HasField("upload_signed_url"):
                    raise Exception(
                        "expected CreateArtifactPartResultMetadata to have upload_signed_url"
                    )

        return response

    def batch_execute_function(
        self, request: BatchExecuteFunctionRequest
    ) -> BatchExecuteFunctionResponse:
        response = self._worker_service.BatchExecuteFunction(request)
        ensure_keys_match(
            expected=request.parameters_by_index,
            actual=response.results_by_index,
        )

        for result in response.results_by_index.values():
            if not result.HasField("kind"):
                raise Exception("expected Value to have kind")

        return response

    def batch_finalize_artifact(
        self, request: BatchFinalizeArtifactRequest
    ) -> BatchFinalizeArtifactResponse:
        response = self._worker_service.BatchFinalizeArtifact(request)
        ensure_keys_match(
            expected=request.configs_by_artifact_id,
            actual=response.results_by_artifact_id,
        )

        return response

    def batch_get_artifact(
        self, request: BatchGetArtifactRequest
    ) -> BatchGetArtifactResponse:
        response = self._worker_service.BatchGetArtifact(request)
        ensure_keys_match(
            expected=request.configs_by_artifact_id,
            actual=response.results_by_artifact_id,
        )

        for result in response.results_by_artifact_id.values():
            if not result.HasField("part_count"):
                raise Exception("expected GetArtifactResult to have part_count")

            if not result.HasField("part_size_threshold"):
                raise Exception(
                    "expected GetArtifactResult to have part_size_threshold"
                )

            if not result.HasField("total_size"):
                raise Exception("expected GetArtifactResult to have total_size")

        return response

    def batch_get_artifact_part(
        self, request: BatchGetArtifactPartRequest
    ) -> BatchGetArtifactPartResponse:
        response = self._worker_service.BatchGetArtifactPart(request)
        ensure_keys_match(
            expected=request.configs_by_artifact_id,
            actual=response.results_by_artifact_id,
        )

        for artifact_id, result in response.results_by_artifact_id.items():
            config = request.configs_by_artifact_id[artifact_id]
            ensure_keys_match(
                expected=config.metadatas_by_part_number,
                actual=result.metadatas_by_part_number,
            )

            for metadata in result.metadatas_by_part_number.values():
                if not metadata.HasField("download_signed_url"):
                    raise Exception(
                        "expected GetArtifactPartResultMetadata to have download_signed_url"
                    )

        return response

    def check_function(self, request: CheckFunctionRequest) -> CheckFunctionResponse:
        return self._worker_service.CheckFunction(request)

    def register_function(
        self, request: RegisterFunctionRequest
    ) -> RegisterFunctionResponse:
        return self._worker_service.RegisterFunction(request)

    def sdk_server_ready(
        self, request: SDKServerReadyRequest
    ) -> SDKServerReadyResponse:
        return self._worker_service.SDKServerReady(request)


# This class is intended to be used for tests and local development
class LocalMessagingClient:
    def batch_create_artifact(
        self, request: BatchCreateArtifactRequest
    ) -> BatchCreateArtifactResponse:
        print(f"sending batch create artifact request: {request}")
        return BatchCreateArtifactResponse()

    def batch_create_artifact_part(
        self, request: BatchCreateArtifactPartRequest
    ) -> BatchCreateArtifactPartResponse:
        print(f"sending batch create artifact part request: {request}")
        return BatchCreateArtifactPartResponse()

    def batch_execute_function(
        self, request: BatchExecuteFunctionRequest
    ) -> BatchExecuteFunctionResponse:
        print(f"sending batch execute function request: {request}")
        return BatchExecuteFunctionResponse()

    def batch_finalize_artifact(
        self, request: BatchFinalizeArtifactRequest
    ) -> BatchFinalizeArtifactResponse:
        print(f"sending batch finalize artifact request: {request}")
        return BatchFinalizeArtifactResponse()

    def batch_get_artifact(
        self, request: BatchGetArtifactRequest
    ) -> BatchGetArtifactResponse:
        print(f"sending batch get artifact request: {request}")
        return BatchGetArtifactResponse()

    def batch_get_artifact_part(
        self, request: BatchGetArtifactPartRequest
    ) -> BatchGetArtifactPartResponse:
        print(f"sending batch get artifact part request: {request}")
        return BatchGetArtifactPartResponse()

    def check_function(self, request: CheckFunctionRequest) -> CheckFunctionResponse:
        print(f"sending check function request: {request}")
        return CheckFunctionResponse()

    def register_function(
        self, request: RegisterFunctionRequest
    ) -> RegisterFunctionResponse:
        print(f"sending register function request: {request}")
        return RegisterFunctionResponse()

    def sdk_server_ready(
        self, request: SDKServerReadyRequest
    ) -> SDKServerReadyResponse:
        print(f"sending sdk server ready request: {request}")
        return SDKServerReadyResponse()
