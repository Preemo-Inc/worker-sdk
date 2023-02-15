from preemo.worker._messaging_client import IMessagingClient, MessagingClient


class TestMessagingClient:
    def test_fulfills_protocol(self) -> None:
        assert isinstance(MessagingClient, IMessagingClient)
