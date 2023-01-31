import zmq

from src.worker_sdk.environment.env_manager import get_required_env


class MessageClient:
    def __init__(self) -> None:
        context = zmq.Context()
        self.__socket = context.socket(zmq.REQ)
        self.__socket.connect(get_required_env("WORKER_SERVER_URL"))

    def send_message(self, message: str) -> str:
        self.__socket.send_string(message)
        reply = self.__socket.recv()

        return reply.decode("utf-8")
