from typing import Callable, Optional

from preemo.gen.endpoints.register_function_pb2 import RegisterFunctionRequest
from preemo.gen.models.registered_function_pb2 import RegisteredFunction
from preemo.gen.models.status_pb2 import STATUS_ERROR, STATUS_OK, Status
from preemo.worker._function_registry import FunctionRegistry
from preemo.worker._messaging_client import IMessagingClient
from preemo.worker._types import assert_never


class WorkerClient:
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

            response = self._client.register_function(
                RegisterFunctionRequest(
                    function_to_register=RegisteredFunction(
                        name=function_name, namespace=namespace
                    )
                )
            )

            match response.status:
                case Status.STATUS_OK:
                    pass
                case Status.STATUS_ERROR | Status.STATUS_UNSPECIFIED:
                    raise Exception(
                        f"worker server replied to register function request with unexpected status: {response.status} and message: {response.message}"
                    )
                case _:
                    assert_never(response.status)
            # if response.status != STATUS_OK:
            #     raise Exception(
            #         f"worker server replied to register function request with unexpected status: {response.status} and message: {response.message}"
            #     )

            return function

        if outer_function is None:
            return decorator

        return decorator(outer_function)
