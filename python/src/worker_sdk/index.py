from typing import Callable, Dict, Optional

from src.gen.worker_request_pb2 import (
    RegisteredFunction,
    RegisterFunctionRequest,
    WorkerRequest,
)
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


class FunctionRegistry:
    def __init__(self) -> None:
        self._global_functions_by_name: Dict[str, Callable] = {}
        self._functions_by_namespace_and_name: Dict[str, Dict[str, Callable]] = {}

    def register_function(
        self, function: Callable, *, name: str, namespace: Optional[str]
    ) -> None:
        if namespace is None:
            if name in self._global_functions_by_name:
                raise Exception(
                    f"must not register multiple functions with the same name: {name}"
                )
            self._global_functions_by_name[name] = function

            return

        if namespace not in self._functions_by_namespace_and_name:
            self._functions_by_namespace_and_name[namespace] = {}
        functions_by_name = self._functions_by_namespace_and_name[namespace]

        if name in functions_by_name:
            raise Exception(
                f"must not register multiple functions with the same namespace: {namespace} and name: {name}"
            )
        functions_by_name[name] = function

    def get_function(self, *, name: str, namespace: Optional[str]) -> Callable:
        if namespace is None:
            function = self._global_functions_by_name.get(name)
            if function is None:
                raise Exception(f"cannot find registered function with name: {name}")

            return function

        function = self._functions_by_namespace_and_name.get(namespace, {}).get(name)
        if function is None:
            raise Exception(
                f"cannot find registered function with namespace: {namespace} and name: {name}"
            )

        return function


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
            # TODO(adrian@preemo.io, 02/15/2023): consider trimming and validating string length for name and namespace
            if name is None:
                function_name = function.__name__
            else:
                function_name = name

            self._function_registry.register_function(
                function, name=function_name, namespace=namespace
            )

            self._client.send_worker_request(
                _construct_register_function_worker_request(
                    name=function_name, namespace=namespace
                )
            )

            # TODO(adrian@preemo.io, 02/15/2023): consider not returning the function
            # that way users cannot call registered functions when registering
            return function

        if outer_function is None:
            return decorator

        return decorator(outer_function)
