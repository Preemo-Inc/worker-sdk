from typing import Callable, Dict, Optional

from src.gen.worker_request_pb2 import (
    RegisteredFunction,
    RegisterFunctionRequest,
    WorkerRequest,
)
from src.worker_sdk.messaging.client import MessagingClient


def _construct_register_function_worker_request(
    *, name: str, namespace: Optional[str]
) -> WorkerRequest:
    function_to_register = RegisteredFunction()
    function_to_register.name = name
    if namespace is not None:
        function_to_register.namespace = namespace

    register_function_request = RegisterFunctionRequest()
    register_function_request.function_to_register = function_to_register

    worker_request = WorkerRequest()
    worker_request.register_function = register_function_request

    return worker_request


# TODO(adrian@preemo.io, 02/03/2023): think of more appropriate name for this class
class Preemo:
    def __init__(self) -> None:
        self._client = MessagingClient()

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
        function: Optional[Callable] = None,
        *,
        name: Optional[str] = None,
        namespace: Optional[str] = None,
    ) -> Callable:
        if function is None:  # caller must have used @register(...)
            if name is None:
                raise ValueError(
                    "name must be specified when calling register explicitly"
                )

        else:  # caller must have used @register
            if name is not None:
                raise Exception("expected name to be None")

            if namespace is not None:
                raise Exception("expected namespace to be None")

            name = function.__name__

        # TODO(adrian@preemo.io, 02/03/2023): consider trimming and validating string length for name and namespace

        self._client.send_worker_request(
            _construct_register_function_worker_request(name=name, namespace=namespace)
        )

        # if namespace is None:
        #     self._global_registered_functions_by_name[name] = function
        # TODO(adrian@preemo.io, 02/03/2023): also add to dictionary

        if function is None:
            return lambda x: x

        return function


preemo = Preemo()

# all public methods of Preemo should be added below for ease of use
register = preemo.register

# TODO(adrian@preemo.io, 02/03/2023): write tests including the following syntaxes
# @register
# @register()
# @register(name=blah)
# @register(namespace=blah)
# @register(name=boo, namespace=blah)
# nested decorators for all these cases
