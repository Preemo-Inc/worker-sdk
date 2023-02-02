from typing import Optional

from src.gen.worker_request_pb2 import RegisteredFunction as ProtoRegisteredFunction
from src.gen.worker_request_pb2 import (
    RegisterFunctionsRequest as ProtoRegisterFunctionsRequest,
)
from src.gen.worker_request_pb2 import WorkerRequest
from src.worker_sdk.request.models import RegisteredFunction, RegisterFunctionsRequest


def try_with_proto_models(*, name: str, namespace: Optional[str]) -> None:
    registered_function = ProtoRegisteredFunction()
    registered_function.name = name
    if namespace is not None:
        registered_function.namespace = namespace

    message_string(registered_function.SerializeToString())


def try_with_base_models(*, name: str, namespace: Optional[str]) -> None:

    pass
