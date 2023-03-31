"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import preemo.gen.models.registered_function_pb2
import preemo.gen.models.value_pb2
import sys
import typing

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class ExecuteFunctionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FUNCTION_TO_EXECUTE_FIELD_NUMBER: builtins.int
    PARAMETER_FIELD_NUMBER: builtins.int
    @property
    def function_to_execute(self) -> preemo.gen.models.registered_function_pb2.RegisteredFunction:
        """Required field specifying which function should be executed."""
    @property
    def parameter(self) -> preemo.gen.models.value_pb2.Value:
        """Required field representing the function parameter."""
    def __init__(
        self,
        *,
        function_to_execute: preemo.gen.models.registered_function_pb2.RegisteredFunction | None = ...,
        parameter: preemo.gen.models.value_pb2.Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_function_to_execute", b"_function_to_execute", "_parameter", b"_parameter", "function_to_execute", b"function_to_execute", "parameter", b"parameter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_function_to_execute", b"_function_to_execute", "_parameter", b"_parameter", "function_to_execute", b"function_to_execute", "parameter", b"parameter"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_function_to_execute", b"_function_to_execute"]) -> typing_extensions.Literal["function_to_execute"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_parameter", b"_parameter"]) -> typing_extensions.Literal["parameter"] | None: ...

global___ExecuteFunctionRequest = ExecuteFunctionRequest

@typing_extensions.final
class ExecuteFunctionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> preemo.gen.models.value_pb2.Value:
        """Required field representing the executed function result."""
    def __init__(
        self,
        *,
        result: preemo.gen.models.value_pb2.Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_result", b"_result", "result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_result", b"_result", "result", b"result"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_result", b"_result"]) -> typing_extensions.Literal["result"] | None: ...

global___ExecuteFunctionResponse = ExecuteFunctionResponse
