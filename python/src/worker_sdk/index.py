from typing import Callable, Optional

from src.gen.worker_request_pb2 import (
    RegisteredFunction,
    RegisterFunctionRequest,
    WorkerRequest,
)
from src.worker_sdk.function_registry import FunctionRegistry
from src.worker_sdk.messaging.client import IMessagingClient


def _construct_register_function_worker_request(
    *, name: str, namespace: Optional[str]
) -> WorkerRequest:
    function_to_register = RegisteredFunction(name=name, namespace=namespace)
    register_function_request = RegisterFunctionRequest(
        function_to_register=function_to_register
    )
    worker_request = WorkerRequest(register_function=register_function_request)

    return worker_request


class PreemoWorkerClient:
    def __init__(self, *, messaging_client: IMessagingClient) -> None:
        self._client = messaging_client
        self._function_registry = FunctionRegistry()

    def register(
        self,
        outer_function: Optional[Callable] = None,
        *,
        name: Optional[str] = None,
        namespace: Optional[str] = None,
    ) -> Callable:
        def decorator(function: Callable) -> Callable:
            if name is None:
                function_name = function.__name__
            else:
                function_name = name

            self._function_registry.register_function(
                function, name=function_name, namespace=namespace
            )

            worker_reply = self._client.send_worker_request(
                _construct_register_function_worker_request(
                    name=function_name, namespace=namespace
                )
            )

            # TODO(adrian@preemo.io, 02/08/2023): finish this
            # if worker_reply.register_function.status !=

            return function

        if outer_function is None:
            return decorator

        return decorator(outer_function)
