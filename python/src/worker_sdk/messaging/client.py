import zmq

from src.worker_sdk.environment.manager import get_required_env


class MessagingClient:
    def __init__(self) -> None:
        context = zmq.Context()
        self._socket = context.socket(zmq.REQ)
        self._socket.connect(get_required_env("PREEMO_WORKER_SERVER_URL"))

    def send_message(self, message: str) -> str:
        self._socket.send_string(message)
        reply = self._socket.recv()

        return reply.decode("utf-8")
