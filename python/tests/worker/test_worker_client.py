from preemo.gen.endpoints.batch_create_artifact_part_pb2 import (
    BatchCreateArtifactPartRequest,
    BatchCreateArtifactPartResponse,
)
from preemo.gen.endpoints.batch_create_artifact_pb2 import (
    BatchCreateArtifactRequest,
    BatchCreateArtifactResponse,
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
from preemo.gen.endpoints.register_function_pb2 import (
    RegisterFunctionRequest,
    RegisterFunctionResponse,
)
from preemo.worker._messaging_client import IMessagingClient
from preemo.worker._worker_client import WorkerClient


class DoNothingMessagingClient(IMessagingClient):
    def batch_create_artifact(
        self, request: BatchCreateArtifactRequest
    ) -> BatchCreateArtifactResponse:
        raise Exception("no call expected")

    def batch_create_artifact_part(
        self, request: BatchCreateArtifactPartRequest
    ) -> BatchCreateArtifactPartResponse:
        raise Exception("no call expected")

    def batch_get_artifact(
        self, request: BatchGetArtifactRequest
    ) -> BatchGetArtifactResponse:
        raise Exception("no call expected")

    def batch_get_artifact_part(
        self, request: BatchGetArtifactPartRequest
    ) -> BatchGetArtifactPartResponse:
        raise Exception("no call expected")

    def check_function(self, request: CheckFunctionRequest) -> CheckFunctionResponse:
        raise Exception("no call expected")

    def execute_function(
        self, request: ExecuteFunctionRequest
    ) -> ExecuteFunctionResponse:
        raise Exception("no call expected")

    def register_function(
        self, request: RegisterFunctionRequest
    ) -> RegisterFunctionResponse:
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
                match send_request_call_count:
                    case 1:
                        assert func.name == "inner_func"
                        assert not func.HasField("namespace")
                    case 2:
                        assert func.name == "inner_func2"
                        assert not func.HasField("namespace")
                    case 3:
                        assert func.name == "another_name"
                        assert not func.HasField("namespace")
                    case 4:
                        assert func.name == "inner_func4"
                        assert func.namespace == "another_namespace"
                    case 5:
                        assert func.name == "another_name"
                        assert func.namespace == "another_namespace"
                    case _:
                        raise Exception(
                            f"unexpected call count: {send_request_call_count}"
                        )

                return RegisterFunctionResponse()

        worker_client = WorkerClient(messaging_client=MockMessagingClient())

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
                match send_request_call_count:
                    case 1:
                        assert func.name == "inner_func"
                        assert not func.HasField("namespace")
                    case 2:
                        assert func.name == "inner_func2"
                        assert not func.HasField("namespace")
                    case 3:
                        assert func.name == "second"
                        assert not func.HasField("namespace")
                    case 4:
                        assert func.name == "third"
                        assert not func.HasField("namespace")
                    case _:
                        raise Exception(
                            f"unexpected call count: {send_request_call_count}"
                        )

                return RegisterFunctionResponse()

        worker_client = WorkerClient(messaging_client=MockMessagingClient())

        class InnerClass:
            @worker_client.register
            @staticmethod
            def inner_func() -> None:
                pass

        assert send_request_call_count == 1

        @worker_client.register(name="third")
        @worker_client.register(name="second")
        @worker_client.register
        def inner_func2() -> None:
            pass

        assert send_request_call_count == 4
