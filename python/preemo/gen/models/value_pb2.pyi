"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.struct_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Value(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NULL_VALUE_FIELD_NUMBER: builtins.int
    ARTIFACT_ID_FIELD_NUMBER: builtins.int
    null_value: google.protobuf.struct_pb2.NullValue.ValueType
    artifact_id: builtins.str
    """Unique identifier for a file stored in the cloud."""
    def __init__(
        self,
        *,
        null_value: google.protobuf.struct_pb2.NullValue.ValueType = ...,
        artifact_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["artifact_id", b"artifact_id", "kind", b"kind", "null_value", b"null_value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["artifact_id", b"artifact_id", "kind", b"kind", "null_value", b"null_value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["kind", b"kind"]) -> typing_extensions.Literal["null_value", "artifact_id"] | None: ...

global___Value = Value
