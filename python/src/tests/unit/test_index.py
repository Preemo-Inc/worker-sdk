from src.gen.worker_request_pb2 import WorkerRequest
from src.worker_sdk.index import Preemo
from src.worker_sdk.messaging.client import IMessagingClient


class TestRegister:
    def test_param_variations(self) -> None:
        send_request_call_count = 0

        class MockMessagingClient(IMessagingClient):
            def send_worker_request(self, worker_request: WorkerRequest) -> None:
                nonlocal send_request_call_count
                send_request_call_count += 1

                func = worker_request.register_function.function_to_register
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

        messaging_client = MockMessagingClient()
        preemo = Preemo(messaging_client=messaging_client)

        @preemo.register
        def inner_func() -> None:
            pass

        assert send_request_call_count == 1

        @preemo.register()
        def inner_func2() -> None:
            pass

        assert send_request_call_count == 2

        @preemo.register(name="another_name")
        def inner_func3() -> None:
            pass

        assert send_request_call_count == 3

        @preemo.register(namespace="another_namespace")
        def inner_func4() -> None:
            pass

        assert send_request_call_count == 4

        @preemo.register(name="another_name", namespace="another_namespace")
        def inner_func5() -> None:
            pass

        assert send_request_call_count == 5
