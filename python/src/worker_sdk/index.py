import functools
from typing import Any, Callable, Dict, Optional

from src.gen.worker_request_pb2 import (
    RegisteredFunction,
    RegisterFunctionRequest,
    WorkerRequest,
)
from src.worker_sdk.messaging.client import IMessagingClient


def _construct_register_function_worker_request(
    *, name: str, namespace: Optional[str]
) -> WorkerRequest:
    function_to_register = RegisteredFunction()
    function_to_register.name = name
    if namespace is not None:
        function_to_register.namespace = namespace

    register_function_request = RegisterFunctionRequest()
    register_function_request.function_to_register.CopyFrom(function_to_register)

    worker_request = WorkerRequest()
    worker_request.register_function.CopyFrom(register_function_request)

    return worker_request


class PreemoWorkerClient:
    def __init__(self, *, messaging_client: IMessagingClient) -> None:
        self._client = messaging_client

        # TODO(adrian@preemo.io, 02/03/2023): consider the best way to handle globals
        # could also just use uuid locally
        self._global_registered_functions_by_name: Dict[str, Callable] = {}
        self._registered_functions_by_namespace_and_name: Dict[
            str, Dict[str, Callable]
        ] = {}

    # TODO(adrian@preemo.io, 02/03/2023): add documentation to the readme explaining how to correctly use this method
    # explain that name must be included if namespace is?
    # explain how to correctly "nest" decorators
    def register(
        self,
        outer_function: Optional[Callable] = None,
        *,
        name: Optional[str] = None,
        namespace: Optional[str] = None,
    ) -> Callable:
        def decorator(function: Callable) -> Callable:
            # TODO(adrian@preemo.io, 02/03/2023): consider trimming and validating string length for name and namespace

            if name is None:
                function_name = function.__name__
            else:
                function_name = name

            if namespace is None:
                if function_name in self._global_registered_functions_by_name:
                    raise Exception(
                        f"must not register multiple functions with the same name: {function_name}"
                    )
                self._global_registered_functions_by_name[function_name] = function

            else:
                if namespace not in self._registered_functions_by_namespace_and_name:
                    self._registered_functions_by_namespace_and_name[namespace] = {}
                registered_functions_by_name = (
                    self._registered_functions_by_namespace_and_name[namespace]
                )

                if function_name in registered_functions_by_name:
                    raise Exception(
                        f"must not register multiple functions with the same namespace: {namespace} and name: {function_name}"
                    )
                registered_functions_by_name[function_name] = function

            self._client.send_worker_request(
                _construct_register_function_worker_request(
                    name=function_name, namespace=namespace
                )
            )

            @functools.wraps(function)
            # TODO(adrian@preemo.io, 02/03/2023): can i avoid using Any here?
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                # TODO(adrian@preemo.io, 02/03/2023): consider not calling the function
                # that way users cannot call registered functions when registering
                return function(*args, **kwargs)

            return wrapper

        if outer_function is None:
            return decorator

        return decorator(outer_function)
