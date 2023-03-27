from concurrent import futures

import grpc

from preemo.gen.services.sdk_pb2_grpc import add_SDKServiceServicer_to_server
from preemo.worker._sdk_service import SDKService


class SDKServer:
    def __init__(self, *, sdk_server_url: str) -> None:
        self._server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
        add_SDKServiceServicer_to_server(SDKService(), self._server)

        # TODO(adrian@preemo.io, 03/27/2023): investigate whether it makes sense to use add_secure_port instead
        self._server.add_insecure_port(sdk_server_url)
        self._server.start()
