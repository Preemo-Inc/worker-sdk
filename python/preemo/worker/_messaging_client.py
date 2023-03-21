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
from preemo.gen.endpoints.execute_function_pb2 import (
    ExecuteFunctionRequest,
    ExecuteFunctionResponse,
)
from preemo.gen.endpoints.header_pb2 import HeaderRequest, HeaderResponse
from preemo.gen.endpoints.register_function_pb2 import (
    RegisterFunctionRequest,
    RegisterFunctionResponse,
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

    def execute_function(
        self, request: ExecuteFunctionRequest
    ) -> ExecuteFunctionResponse:
        pass

    def register_function(
        self, request: RegisterFunctionRequest
    ) -> RegisterFunctionResponse:
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

        return response

    def batch_create_artifact_part(
        self, request: BatchCreateArtifactPartRequest
    ) -> BatchCreateArtifactPartResponse:
        response = self._worker_service.BatchCreateArtifactPart(request)
        ensure_keys_match(
            expected=request.configs_by_artifact_id,
            actual=response.results_by_artifact_id,
        )

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

        return response

    def batch_get_artifact_part(
        self, request: BatchGetArtifactPartRequest
    ) -> BatchGetArtifactPartResponse:
        response = self._worker_service.BatchGetArtifactPart(request)
        ensure_keys_match(
            expected=request.configs_by_artifact_id,
            actual=response.results_by_artifact_id,
        )

        return response

    def check_function(self, request: CheckFunctionRequest) -> CheckFunctionResponse:
        return self._worker_service.CheckFunction(request)

    def execute_function(
        self, request: ExecuteFunctionRequest
    ) -> ExecuteFunctionResponse:
        response = self._worker_service.ExecuteFunction(request)
        ensure_keys_match(
            expected=request.parameters_by_index,
            actual=response.results_by_index,
        )

        return response

    def register_function(
        self, request: RegisterFunctionRequest
    ) -> RegisterFunctionResponse:
        return self._worker_service.RegisterFunction(request)


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

    def execute_function(
        self, request: ExecuteFunctionRequest
    ) -> ExecuteFunctionResponse:
        print(f"sending execute function request: {request}")
        return ExecuteFunctionResponse()

    def register_function(
        self, request: RegisterFunctionRequest
    ) -> RegisterFunctionResponse:
        print(f"sending register function request: {request}")
        return RegisterFunctionResponse()
