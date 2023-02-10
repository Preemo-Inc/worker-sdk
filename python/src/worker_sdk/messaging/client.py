from typing import Protocol, runtime_checkable

import zmq

from src.gen.header_pb2 import HeaderReply, HeaderRequest
from src.gen.shared_pb2 import STATUS_OK
from src.gen.worker_reply_pb2 import WorkerReply
from src.gen.worker_request_pb2 import WorkerRequest


@runtime_checkable
class IMessagingClient(Protocol):
    def send_worker_request(self, worker_request: WorkerRequest) -> WorkerReply:
        pass


class MessagingClient:
    def __init__(self, *, version: str, worker_server_url: str) -> None:
        context = zmq.Context()

        # TODO(adrian@preemo.io, 02/25/2023): investigate other socket types, such as PUSH/PULL
        self._socket = context.socket(zmq.REQ)
        self._socket.connect(worker_server_url)

        header_reply = self._send_header_request(HeaderRequest(version=version))
        if header_reply.status != STATUS_OK:
            raise Exception(
                f"worker server replied to header request with unexpected status: {header_reply.status} and message: {header_reply.message}"
            )

    def _send_message(self, message: bytes) -> bytes:
        self._socket.send(message)
        return self._socket.recv()

    def _send_header_request(self, header_request: HeaderRequest) -> HeaderReply:
        message = header_request.SerializeToString()
        reply = self._send_message(message)

        return HeaderReply.FromString(reply)

    def send_worker_request(self, worker_request: WorkerRequest) -> WorkerReply:
        message = worker_request.SerializeToString()
        reply = self._send_message(message)

        return WorkerReply.FromString(reply)
