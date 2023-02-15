import pkg_resources

from preemo.worker._env import get_required_env as _get_required_env
from preemo.worker._messaging_client import MessagingClient as _MessagingClient
from preemo.worker._worker_client import WorkerClient as _WorkerClient

__all__ = ["register"]

_worker_client = _WorkerClient(
    messaging_client=_MessagingClient(
        version=pkg_resources.get_distribution("preemo_worker_sdk").version,
        worker_server_url=_get_required_env("PREEMO_WORKER_SERVER_URL"),
    )
)

register = _worker_client.register
