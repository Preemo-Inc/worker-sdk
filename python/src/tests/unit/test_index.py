from src.gen.worker_request_pb2 import WorkerRequest
from src.worker_sdk.index import Preemo
from src.worker_sdk.messaging.client import IMessagingClient


class MockMessagingClient(IMessagingClient):
    def send_worker_request(self, worker_request: WorkerRequest) -> None:
        pass


class TestRegister:
    def test_something(self) -> None:
        mock_messaging_client = MockMessagingClient()
        preemo = Preemo(messaging_client=mock_messaging_client)

        @preemo.register
        def inner_func() -> None:
            pass
