from preemo.worker._messaging_client import (
    IMessagingClient,
    LocalMessagingClient,
    MessagingClient,
)


class TestMessagingClient:
    def test_fulfills_protocol(self) -> None:
        assert isinstance(MessagingClient, IMessagingClient)


class TestLocalMessagingClient:
    def test_fulfills_protocol(self) -> None:
        assert isinstance(LocalMessagingClient, IMessagingClient)
