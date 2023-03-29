import threading
from typing import Optional

from preemo.worker._artifact_manager import ArtifactManager as _ArtifactManager
from preemo.worker._env import get_optional_env as _get_optional_env
from preemo.worker._messaging_client import IMessagingClient as _IMessagingClient
from preemo.worker._messaging_client import (
    LocalMessagingClient as _LocalMessagingClient,
)
from preemo.worker._messaging_client import MessagingClient as _MessagingClient
from preemo.worker._sdk_server import SDKServer as _SDKServer
from preemo.worker._worker_client import WorkerClient as _WorkerClient

__all__ = ["get_function", "parallelize", "register"]


def _start_sdk_server() -> Optional[_SDKServer]:
    sdk_server_host = _get_optional_env("PREEMO_SDK_SERVER_HOST")
    if sdk_server_host is None:
        return None

    server = _SDKServer(sdk_server_host=sdk_server_host)
    # This thread will keep the process running until the server is closed
    threading.Thread(target=lambda: server.wait_until_close()).start()

    return server


def _construct_messaging_client(*, sdk_server_port: Optional[int]) -> _IMessagingClient:
    worker_server_url = _get_optional_env("PREEMO_WORKER_SERVER_URL")

    if worker_server_url is None:
        return _LocalMessagingClient()

    return _MessagingClient(
        sdk_server_port=sdk_server_port, worker_server_url=worker_server_url
    )


_sdk_server = _start_sdk_server()
_sdk_server_port = None if _sdk_server is None else _sdk_server.get_port()

_messaging_client = _construct_messaging_client(sdk_server_port=_sdk_server_port)
_artifact_manager = _ArtifactManager(messaging_client=_messaging_client)
_worker_client = _WorkerClient(
    artifact_manager=_artifact_manager, messaging_client=_messaging_client
)

get_function = _worker_client.get_function
parallelize = _worker_client.parallelize
register = _worker_client.register
