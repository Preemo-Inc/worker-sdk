from typing import Protocol, runtime_checkable

from grpclib.client import Channel

from preemo import __version__
from preemo.gen.endpoints import (
    HeaderRequest,
    HeaderResponse,
    RegisterFunctionRequest,
    RegisterFunctionResponse,
)
from preemo.gen.models import Status
from preemo.gen.services import WorkerServiceStub


@runtime_checkable
class IMessagingClient(Protocol):
    async def register_function(
        self, request: RegisterFunctionRequest
    ) -> RegisterFunctionResponse:
        pass


class MessagingClient:
    # TODO(adrian@preemo.io, 03/06/2023): add something to prevent users from calling constructor?
    def __init__(self, *, worker_server_host: str, worker_server_port: int) -> None:
        self._channel = Channel(host=worker_server_host, port=worker_server_port)
        self._worker_service = WorkerServiceStub(self._channel)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(get_chat_id("django"))

    @classmethod
    async def create(cls, *, worker_server_host: str, worker_server_port: int):
        a = cls(
            worker_server_host=worker_server_host, worker_server_port=worker_server_port
        )
        header_response = a._initiate(HeaderRequest(version=__version__))
        if header_response.status != Status.STATUS_OK:
            raise Exception(
                f"worker server replied to header request with unexpected status: {header_response.status} and message: {header_response.message}"
            )

    async def _initiate(self, request: HeaderRequest) -> HeaderResponse:
        return await self._worker_service.initiate(request)

    def register_function(
        self, request: RegisterFunctionRequest
    ) -> RegisterFunctionResponse:
        # TODO(adrian@preemo.io, 03/03/2023): can we do better with the types?
        return self._worker_service.RegisterFunction(request)  # type: ignore


# This class is intended to be used for tests and local development
class LocalMessagingClient:
    def register_function(
        self, request: RegisterFunctionRequest
    ) -> RegisterFunctionResponse:
        print(f"sending register function request: {request}")
        return RegisterFunctionResponse(status=STATUS_OK)
