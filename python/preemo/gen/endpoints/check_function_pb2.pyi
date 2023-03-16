"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import preemo.gen.models.registered_function_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class CheckFunctionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FUNCTION_TO_CHECK_FIELD_NUMBER: builtins.int
    @property
    def function_to_check(self) -> preemo.gen.models.registered_function_pb2.RegisteredFunction: ...
    def __init__(
        self,
        *,
        function_to_check: preemo.gen.models.registered_function_pb2.RegisteredFunction | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_function_to_check", b"_function_to_check", "function_to_check", b"function_to_check"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_function_to_check", b"_function_to_check", "function_to_check", b"function_to_check"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_function_to_check", b"_function_to_check"]) -> typing_extensions.Literal["function_to_check"] | None: ...

global___CheckFunctionRequest = CheckFunctionRequest

@typing_extensions.final
class CheckFunctionResponse(google.protobuf.message.Message):
    """A successful response indicates the function is registered.
    If the function is not regsitered, a NOT_FOUND status will be thrown.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___CheckFunctionResponse = CheckFunctionResponse
