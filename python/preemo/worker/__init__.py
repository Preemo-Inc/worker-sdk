import threading
from typing import Optional

from preemo.gen.endpoints.sdk_server_ready_pb2 import (
    SDKServerReadyRequest as _SDKServerReadyRequest,
)
from preemo.worker._artifact_manager import ArtifactManager as _ArtifactManager
from preemo.worker._env import get_optional_env as _get_optional_env
from preemo.worker._function_registry import FunctionRegistry as _FunctionRegistry
from preemo.worker._messaging_client import IMessagingClient as _IMessagingClient
from preemo.worker._messaging_client import (
    LocalMessagingClient as _LocalMessagingClient,
)
from preemo.worker._messaging_client import MessagingClient as _MessagingClient
from preemo.worker._sdk_server import SDKServer as _SDKServer
from preemo.worker._worker_client import WorkerClient as _WorkerClient


def _construct_messaging_client() -> _IMessagingClient:
    worker_server_url = _get_optional_env("PREEMO_WORKER_SERVER_URL")

    if worker_server_url is None:
        return _LocalMessagingClient()

    return _MessagingClient(worker_server_url=worker_server_url)


def _start_sdk_server(
    *, artifact_manager: _ArtifactManager, function_registry: _FunctionRegistry
) -> Optional[_SDKServer]:
    sdk_server_host = _get_optional_env("PREEMO_SDK_SERVER_HOST")
    if sdk_server_host is None:
        return None

    server = _SDKServer(
        artifact_manager=artifact_manager,
        function_registry=function_registry,
        sdk_server_host=sdk_server_host,
    )
    # This thread will keep the process running until the server is closed
    threading.Thread(target=lambda: server.wait_until_close()).start()

    return server


def _construct_worker_client() -> _WorkerClient:
    messaging_client = _construct_messaging_client()
    artifact_manager = _ArtifactManager(messaging_client=messaging_client)

    function_registry = _FunctionRegistry()
    sdk_server = _start_sdk_server(
        artifact_manager=artifact_manager, function_registry=function_registry
    )

    if sdk_server is not None:
        messaging_client.sdk_server_ready(
            _SDKServerReadyRequest(sdk_server_port=sdk_server.get_port())
        )

    return _WorkerClient(
        artifact_manager=artifact_manager,
        function_registry=function_registry,
        messaging_client=messaging_client,
    )


# provide shorthand for functions
__all__ = ["get_function", "parallel", "register"]

_worker_client = _construct_worker_client()

get_function = _worker_client.get_function
parallel = _worker_client.parallel
register = _worker_client.register
