import pytest
from pytest import MonkeyPatch
from pytest_mock import MockerFixture

from src.gen.worker_request_pb2 import WorkerRequest
from src.worker_sdk.index import Preemo
from src.worker_sdk.messaging.client import MessagingClientProtocol


class MockMessagingClient(MessagingClientProtocol):
    def send_worker_request(self, worker_request: WorkerRequest) -> None:
        pass


class TestRegister:
    # before each
    @pytest.fixture(autouse=True)
    def setup_env(self, monkeypatch: MonkeyPatch) -> None:
        monkeypatch.setenv("MOCK_VAR", "anything")

    def test_something(self, mocker: MockerFixture) -> None:
        # mock_messaging_client = MockMessagingClient()
        # preemo = Preemo(messaging_client=mock_messaging_client)
        # def mock_init():
        #     return None

        # mock_messaging_client = mocker.patch(
        #     "src.worker_sdk.messaging.client.MessagingClient.__init__",
        #     return_value=None,
        # )
        # print(mock_messaging_client.call_count)
        # preemo = Preemo()
        # print(mock_messaging_client.call_count)
        # assert False
        # preemo.register
