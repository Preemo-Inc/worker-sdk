from typing import Callable, Optional

from preemo.gen.endpoints.check_function_pb2 import CheckFunctionRequest
from preemo.gen.endpoints.register_function_pb2 import RegisterFunctionRequest
from preemo.gen.models.registered_function_pb2 import RegisteredFunction
from preemo.worker._function_registry import FunctionRegistry
from preemo.worker._messaging_client import IMessagingClient


class Function:
    def __init__(
        self, *, messaging_client: IMessagingClient, name: str, namespace: Optional[str]
    ) -> None:
        self._client = messaging_client
        self._name = name
        self._namespace = namespace

        self._ensure_function_is_registered()

    def _ensure_function_is_registered(self) -> None:
        # check_function raises an error if the function is not found
        self._client.check_function(
            CheckFunctionRequest(
                registered_function=RegisteredFunction(
                    name=self._name, namespace=self._namespace
                )
            )
        )

    def __call__(self, params: Optional[str] = None) -> Optional[str]:
        if params is not None:
            # TODO(adrian@preemo.io, 03/08/2023): create thing
            pass

        # TODO(adrian@preemo.io, 03/08/2023):
        # send request to worker to execute request
        # wait for response and return it
        raise Exception("not yet implemented")


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

            self._client.register_function(
                RegisterFunctionRequest(
                    function_to_register=RegisteredFunction(
                        name=function_name, namespace=namespace
                    )
                )
            )

            return function

        if outer_function is None:
            return decorator

        return decorator(outer_function)

    def get_function(self, name: str, *, namespace: Optional[str] = None) -> Function:
        return Function(messaging_client=self._client, name=name, namespace=namespace)

    def parallelize(self, function: Function, params: list[str]) -> list[Optional[str]]:
        if len(params) == 0:
            return []

        # TODO(adrian@preemo.io, 03/08/2023):
        # ask worker to parallelize function with params
        raise Exception("not yet implemented")
