from typing import Protocol, runtime_checkable

import grpc

from preemo import __version__
from preemo.gen.models.status_pb2 import STATUS_OK
from preemo.gen.requests.header_pb2 import HeaderRequest, HeaderResponse
from preemo.gen.requests.register_function_pb2 import (
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
        self._channel = grpc.insecure_channel(target=worker_server_url)
        self._worker_service = WorkerServiceStub(self._channel)

        header_response = self._initiate(HeaderRequest(version=__version__))
        if header_response.status != STATUS_OK:
            raise Exception(
                f"worker server replied to header request with unexpected status: {header_response.status} and message: {header_response.message}"
            )

    def _initiate(self, request: HeaderRequest) -> HeaderResponse:
        return self._worker_service.Initiate(request)  # type: ignore

    def register_function(
        self, request: RegisterFunctionRequest
    ) -> RegisterFunctionResponse:
        # TODO(adrian@preemo.io, 03/03/2023): can we do better with the types?
        return self._worker_service.RegisterFunction(request)  # type: ignore


# TODO(adrian@preemo.io, 03/03/2023): do we need this?
# # This class is intended to be used for tests and local development
# class LocalMessagingClient:
#     def send_worker_request(self, worker_request: WorkerRequest) -> WorkerReply:
#         print(f"sending worker request: {worker_request}")
#         # TODO(adrian@preemo.io, 02/15/2023): have this send a different reply for different request types
#         return WorkerReply(register_function=RegisterFunctionReply(status=STATUS_OK))
