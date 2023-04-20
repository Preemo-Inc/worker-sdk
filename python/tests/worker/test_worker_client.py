from typing import List

from preemo.gen.endpoints.batch_allocate_artifact_part_pb2 import (
    BatchAllocateArtifactPartRequest,
    BatchAllocateArtifactPartResponse,
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
from preemo.gen.endpoints.batch_get_artifact_download_url_pb2 import (
    BatchGetArtifactDownloadUrlRequest,
    BatchGetArtifactDownloadUrlResponse,
)
from preemo.gen.endpoints.batch_get_artifact_pb2 import (
    BatchGetArtifactRequest,
    BatchGetArtifactResponse,
)
from preemo.gen.endpoints.batch_get_artifact_upload_url_pb2 import (
    BatchGetArtifactUploadUrlRequest,
    BatchGetArtifactUploadUrlResponse,
)
from preemo.gen.endpoints.check_function_pb2 import (
    CheckFunctionRequest,
    CheckFunctionResponse,
)
from preemo.gen.endpoints.register_function_pb2 import (
    RegisterFunctionRequest,
    RegisterFunctionResponse,
)
from preemo.gen.endpoints.sdk_server_ready_pb2 import (
    SdkServerReadyRequest,
    SdkServerReadyResponse,
)
from preemo.worker._artifact_manager import ArtifactId, IArtifactManager
from preemo.worker._function_registry import FunctionRegistry
from preemo.worker._messaging_client import IMessagingClient
from preemo.worker._worker_client import WorkerClient


class DoNothingArtifactManager(IArtifactManager):
    def create_artifact(self, content: bytes) -> ArtifactId:
        raise Exception("no call expected")

    def create_artifacts(self, contents: List[bytes]) -> List[ArtifactId]:
        raise Exception("no call expected")

    def get_artifact(self, artifact_id: ArtifactId) -> bytes:
        raise Exception("no call expected")

    def get_artifacts(self, artifact_ids: List[ArtifactId]) -> List[bytes]:
        raise Exception("no call expected")


class DoNothingMessagingClient(IMessagingClient):
    def batch_allocate_artifact_part(
        self, request: BatchAllocateArtifactPartRequest
    ) -> BatchAllocateArtifactPartResponse:
        raise Exception("no call expected")

    def batch_create_artifact(
        self, request: BatchCreateArtifactRequest
    ) -> BatchCreateArtifactResponse:
        raise Exception("no call expected")

    def batch_execute_function(
        self, request: BatchExecuteFunctionRequest
    ) -> BatchExecuteFunctionResponse:
        raise Exception("no call expected")

    def batch_finalize_artifact(
        self, request: BatchFinalizeArtifactRequest
    ) -> BatchFinalizeArtifactResponse:
        raise Exception("no call expected")

    def batch_get_artifact(
        self, request: BatchGetArtifactRequest
    ) -> BatchGetArtifactResponse:
        raise Exception("no call expected")

    def batch_get_artifact_download_url(
        self, request: BatchGetArtifactDownloadUrlRequest
    ) -> BatchGetArtifactDownloadUrlResponse:
        raise Exception("no call expected")

    def batch_get_artifact_upload_url(
        self, request: BatchGetArtifactUploadUrlRequest
    ) -> BatchGetArtifactUploadUrlResponse:
        raise Exception("no call expected")

    def check_function(self, request: CheckFunctionRequest) -> CheckFunctionResponse:
        raise Exception("no call expected")

    def register_function(
        self, request: RegisterFunctionRequest
    ) -> RegisterFunctionResponse:
        raise Exception("no call expected")

    def sdk_server_ready(
        self, request: SdkServerReadyRequest
    ) -> SdkServerReadyResponse:
        raise Exception("no call expected")


class TestRegister:
    def test_param_variations(self) -> None:
        send_request_call_count = 0

        class MockMessagingClient(DoNothingMessagingClient):
            def register_function(
                self, request: RegisterFunctionRequest
            ) -> RegisterFunctionResponse:
                nonlocal send_request_call_count
                send_request_call_count += 1

                func = request.function_to_register
                if send_request_call_count == 1:
                    assert func.name == "inner_func"
                    assert not func.HasField("namespace")
                elif send_request_call_count == 2:
                    assert func.name == "inner_func2"
                    assert not func.HasField("namespace")
                elif send_request_call_count == 3:
                    assert func.name == "another_name"
                    assert not func.HasField("namespace")
                elif send_request_call_count == 4:
                    assert func.name == "inner_func4"
                    assert func.namespace == "another_namespace"
                elif send_request_call_count == 5:
                    assert func.name == "another_name"
                    assert func.namespace == "another_namespace"
                else:
                    raise Exception(f"unexpected call count: {send_request_call_count}")

                return RegisterFunctionResponse()

        worker_client = WorkerClient(
            artifact_manager=DoNothingArtifactManager(),
            function_registry=FunctionRegistry(),
            messaging_client=MockMessagingClient(),
        )

        @worker_client.register
        def inner_func() -> None:
            pass

        assert send_request_call_count == 1

        @worker_client.register()
        def inner_func2() -> None:
            pass

        assert send_request_call_count == 2

        @worker_client.register(name="another_name")
        def inner_func3() -> None:
            pass

        assert send_request_call_count == 3

        @worker_client.register(namespace="another_namespace")
        def inner_func4() -> None:
            pass

        assert send_request_call_count == 4

        @worker_client.register(name="another_name", namespace="another_namespace")
        def inner_func5() -> None:
            pass

        assert send_request_call_count == 5

    def test_nested_decorators(self) -> None:
        send_request_call_count = 0

        class MockMessagingClient(DoNothingMessagingClient):
            def register_function(
                self, request: RegisterFunctionRequest
            ) -> RegisterFunctionResponse:
                nonlocal send_request_call_count
                send_request_call_count += 1

                func = request.function_to_register
                if send_request_call_count == 1:
                    assert func.name == "inner_func"
                    assert not func.HasField("namespace")
                elif send_request_call_count == 2:
                    assert func.name == "inner_func2"
                    assert not func.HasField("namespace")
                elif send_request_call_count == 3:
                    assert func.name == "second"
                    assert not func.HasField("namespace")
                elif send_request_call_count == 4:
                    assert func.name == "third"
                    assert not func.HasField("namespace")
                else:
                    raise Exception(f"unexpected call count: {send_request_call_count}")

                return RegisterFunctionResponse()

        worker_client = WorkerClient(
            artifact_manager=DoNothingArtifactManager(),
            function_registry=FunctionRegistry(),
            messaging_client=MockMessagingClient(),
        )

        class InnerClass:
            @staticmethod
            @worker_client.register
            def inner_func() -> None:
                pass

        assert send_request_call_count == 1

        @worker_client.register(name="third")
        @worker_client.register(name="second")
        @worker_client.register
        def inner_func2() -> None:
            pass

        assert send_request_call_count == 4
