from typing import Protocol, runtime_checkable

import zmq

from src.gen.worker_request_pb2 import WorkerRequest


@runtime_checkable
class IMessagingClient(Protocol):
    def send_worker_request(self, worker_request: WorkerRequest) -> None:
        pass


class MessagingClient:
    def __init__(self, *, worker_server_url: str) -> None:
        context = zmq.Context()
        # TODO(adrian@preemo.io, 02/25/2023): investigate other socket types, such as PUSH/PULL
        self._socket = context.socket(zmq.REQ)
        self._socket.connect(worker_server_url)
        # TODO(adrian@preemo.io, 02/15/2023): send header as first message
        # header should contain metadata such as version

    def _send_message(self, message: bytes) -> bytes:
        self._socket.send(message)
        return self._socket.recv()

    def send_worker_request(self, worker_request: WorkerRequest) -> None:
        message = worker_request.SerializeToString()

        # TODO(adrian@preemo.io, 02/15/2023): validate reply
        self._send_message(message)

        # TODO(adrian@preemo.io, 02/15/2023): consider returning object indicating success?
