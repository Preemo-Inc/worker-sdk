from typing import Callable

import grpc

from preemo.gen.endpoints.execute_function_pb2 import (
    ExecuteFunctionRequest,
    ExecuteFunctionResponse,
)
from preemo.gen.endpoints.terminate_pb2 import TerminateRequest, TerminateResponse
from preemo.gen.services.sdk_pb2_grpc import SDKServiceServicer
from preemo.worker._function_registry import FunctionRegistry


class SDKService(SDKServiceServicer):
    def __init__(
        self,
        *,
        function_registry: FunctionRegistry,
        terminate_server: Callable[[], None]
    ) -> None:
        self._function_registry = function_registry
        self._terminate_server = terminate_server

    def ExecuteFunction(
        self, request: ExecuteFunctionRequest, context: grpc.ServicerContext
    ) -> ExecuteFunctionResponse:
        if not request.HasField("function_to_execute"):
            raise Exception(
                "expected execute function request to have function_to_execute"
            )

        if not request.function_to_execute.HasField("name"):
            raise Exception("expected function_to_execute to have name")

        func = self._function_registry.get_function(
            name=request.function_to_execute.name,
            namespace=request.function_to_execute.namespace,
        )

        # TODO(adrian@preemo.io, 03/28/2023): implement
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError()

    def Terminate(
        self, request: TerminateRequest, context: grpc.ServicerContext
    ) -> TerminateResponse:
        self._terminate_server()
        return TerminateResponse()
