from typing import Protocol, runtime_checkable

import grpc

from preemo import __version__
from preemo.gen.endpoints.header_pb2 import HeaderRequest, HeaderResponse
from preemo.gen.endpoints.register_function_pb2 import (
    RegisterFunctionRequest,
    RegisterFunctionResponse,
)
from preemo.gen.services.worker_pb2_grpc import WorkerServiceStub


@runtime_checkable
class IMessagingClient(Protocol):
    def register_function(
        self, request: RegisterFunctionRequest
    ) -> RegisterFunctionResponse:
        pass


class MessagingClient:
    def __init__(self, *, worker_server_url: str) -> None:
        # TODO(adrian@preemo.io, 03/15/2023): investigate whether it makes sense to use secure_channel instead
        self._channel = grpc.insecure_channel(target=worker_server_url)
        self._worker_service = WorkerServiceStub(self._channel)

        self._initiate(HeaderRequest(version=__version__))

    def _initiate(self, request: HeaderRequest) -> HeaderResponse:
        return self._worker_service.Initiate(request)

    def register_function(
        self, request: RegisterFunctionRequest
    ) -> RegisterFunctionResponse:
        return self._worker_service.RegisterFunction(request)


# This class is intended to be used for tests and local development
class LocalMessagingClient:
    def register_function(
        self, request: RegisterFunctionRequest
    ) -> RegisterFunctionResponse:
        print(f"sending register function request: {request}")
        return RegisterFunctionResponse()
