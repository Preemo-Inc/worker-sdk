from src.gen.worker_request_pb2 import RegisteredFunction as ProtoRegisteredFunction
from src.gen.worker_request_pb2 import (
    RegisterFunctionsRequest as ProtoRegisterFunctionsRequest,
)
from src.gen.worker_request_pb2 import WorkerRequest
from src.worker_sdk.request.models import RegisteredFunction, RegisterFunctionsRequest


def __serialize_registered_function(
    registered_function: RegisteredFunction,
) -> ProtoRegisteredFunction:
    result = ProtoRegisteredFunction()
    result.name = registered_function.name
    if registered_function.namespace is not None:
        result.namespace = registered_function.namespace

    return result


def __serialize_register_functions_request(
    request: RegisterFunctionsRequest,
) -> ProtoRegisterFunctionsRequest:
    result = ProtoRegisterFunctionsRequest()
    result.functions_to_register.extend(
        elem_seq=[
            __serialize_registered_function(registered_function=func)
            for func in request.functions_to_register
        ]
    )

    return result


def serialize_register_functions_request(
    request: RegisterFunctionsRequest,
) -> WorkerRequest:
    result = WorkerRequest()
    result.register_functions = __serialize_register_functions_request(request=request)

    return result
