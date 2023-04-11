import threading
from typing import Optional

from preemo.gen.endpoints.sdk_server_ready_pb2 import (
    SdkServerReadyRequest as _SdkServerReadyRequest,
)
from preemo.worker._artifact_manager import ArtifactManager as _ArtifactManager
from preemo.worker._artifact_manager import IArtifactManager as _IArtifactManager
from preemo.worker._env_manager import EnvManager as _EnvManager
from preemo.worker._function_registry import FunctionRegistry as _FunctionRegistry
from preemo.worker._messaging_client import IMessagingClient as _IMessagingClient
from preemo.worker._messaging_client import (
    LocalMessagingClient as _LocalMessagingClient,
)
from preemo.worker._messaging_client import MessagingClient as _MessagingClient
from preemo.worker._sdk_server import SdkServer as _SdkServer
from preemo.worker._worker_client import WorkerClient as _WorkerClient


def _construct_artifact_manager(
    messaging_client: _IMessagingClient,
) -> _IArtifactManager:
    is_development = _EnvManager.is_development
    if is_development is None:
        is_development = False

    max_download_threads = _EnvManager.max_download_threads
    if max_download_threads is None:
        max_download_threads = 5

    max_upload_threads = _EnvManager.max_upload_threads
    if max_upload_threads is None:
        max_upload_threads = 5

    return _ArtifactManager(
        is_development=is_development,
        max_download_threads=max_download_threads,
        max_upload_threads=max_upload_threads,
        messaging_client=messaging_client,
    )


def _construct_messaging_client() -> _IMessagingClient:
    if _EnvManager.worker_server_url is None:
        return _LocalMessagingClient()

    return _MessagingClient(worker_server_url=_EnvManager.worker_server_url)


def _start_sdk_server(
    *, artifact_manager: _IArtifactManager, function_registry: _FunctionRegistry
) -> Optional[_SdkServer]:
    if _EnvManager.sdk_server_host is None:
        return None

    server = _SdkServer(
        artifact_manager=artifact_manager,
        function_registry=function_registry,
        sdk_server_host=_EnvManager.sdk_server_host,
    )
    # This thread will keep the process running until the server is closed
    threading.Thread(target=lambda: server.wait_until_close()).start()

    return server


def _construct_worker_client() -> _WorkerClient:
    messaging_client = _construct_messaging_client()
    artifact_manager = _construct_artifact_manager(messaging_client=messaging_client)

    function_registry = _FunctionRegistry()
    sdk_server = _start_sdk_server(
        artifact_manager=artifact_manager, function_registry=function_registry
    )

    if sdk_server is not None:
        messaging_client.sdk_server_ready(
            _SdkServerReadyRequest(sdk_server_port=sdk_server.get_port())
        )

    return _WorkerClient(
        artifact_manager=artifact_manager,
        function_registry=function_registry,
        messaging_client=messaging_client,
    )


# TODO(adrian@preemo.io, 04/11/2023): add environment (dev, prod)

# provide shorthand for functions
__all__ = ["get_function", "parallel", "register"]

_worker_client = _construct_worker_client()

get_function = _worker_client.get_function
parallel = _worker_client.parallel
register = _worker_client.register
