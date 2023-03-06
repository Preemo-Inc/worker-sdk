from typing import Callable, Optional

from preemo.gen.endpoints import RegisterFunctionRequest
from preemo.gen.models import RegisteredFunction, Status
from preemo.worker._function_registry import FunctionRegistry
from preemo.worker._messaging_client import IMessagingClient


class WorkerClient:
    def __init__(self, *, messaging_client: IMessagingClient) -> None:
        self._client = messaging_client
        self._function_registry = FunctionRegistry()

    async def register(
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

            response = await self._client.register_function(
                RegisterFunctionRequest(
                    function_to_register=RegisteredFunction(
                        name=function_name, namespace=namespace
                    )
                )
            )

            if response.status != Status.STATUS_OK:
                raise Exception(
                    f"worker server replied to register function request with unexpected status: {response.status} and message: {response.message}"
                )

            return function

        if outer_function is None:
            return decorator

        return decorator(outer_function)
