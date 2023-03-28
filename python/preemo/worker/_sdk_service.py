from typing import Callable

import grpc

from preemo.gen.endpoints.execute_function_pb2 import (
    ExecuteFunctionRequest,
    ExecuteFunctionResponse,
)
from preemo.gen.endpoints.terminate_pb2 import TerminateRequest, TerminateResponse
from preemo.gen.services.sdk_pb2_grpc import SDKServiceServicer


class SDKService(SDKServiceServicer):
    def __init__(self, *, terminate_server: Callable[[], None]) -> None:
        self._terminate_server = terminate_server

    def ExecuteFunction(
        self, request: ExecuteFunctionRequest, context: grpc.ServicerContext
    ) -> ExecuteFunctionResponse:
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError()

    def Terminate(
        self, request: TerminateRequest, context: grpc.ServicerContext
    ) -> TerminateResponse:
        self._terminate_server()
        return TerminateResponse()
