from typing import Callable, Optional

from src.gen.shared_pb2 import STATUS_OK, RegisteredFunction
from src.gen.worker.request_pb2 import RegisterFunctionRequest, WorkerRequest
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

            # TODO(adrian@preemo.io, 02/09/2023): do i need to validate that register_function is set?
            reply = worker_reply.register_function
            if reply.status != STATUS_OK:
                raise Exception(
                    f"worker server replied to register function request with unexpected status: {reply.status} and message: {reply.message}"
                )

            return function

        if outer_function is None:
            return decorator

        return decorator(outer_function)
