# import pytest
# from pytest import MonkeyPatch
# from pytest_mock import MockFixture

# from src.worker_sdk.index import Preemo


# class TestRegister:
#     # before each
#     @pytest.fixture(autouse=True)
#     def setup_env(self, monkeypatch: MonkeyPatch) -> None:
#         monkeypatch.setenv("MOCK_VAR", "anything")

#     def test_retrieves_correct_value(
#         self,
#         mocker: MockFixture,
#     ) -> None:
#         def mock_init():
#             return None

#         mock_messaging_client = mocker.patch(
#             "src.worker_sdk.messaging.client.MessagingClient",
#         )
#         print(mock_messaging_client.call_count)
#         preemo = Preemo()
#         print(mock_messaging_client.call_count)
#         assert False
#         # preemo.register
