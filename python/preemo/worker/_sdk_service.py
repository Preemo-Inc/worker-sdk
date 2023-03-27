from concurrent import futures

import grpc

from preemo.gen.endpoints.execute_function_pb2 import (
    ExecuteFunctionRequest,
    ExecuteFunctionResponse,
)
from preemo.gen.services.sdk_pb2_grpc import (
    SDKServiceServicer,
    add_SDKServiceServicer_to_server,
)


class SDKService(SDKServiceServicer):
    def ExecuteFunction(
        self, request: ExecuteFunctionRequest, context: grpc.ServicerContext
    ) -> ExecuteFunctionResponse:
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError()


# TODO(adrian@preemo.io, 03/27/2023): cleanup
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
servicer = SDKService()
add_SDKServiceServicer_to_server(servicer, server)
