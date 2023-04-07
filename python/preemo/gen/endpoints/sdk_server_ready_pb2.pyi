"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class SdkServerReadyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SDK_SERVER_PORT_FIELD_NUMBER: builtins.int
    sdk_server_port: builtins.int
    """Required field for the port on which the SDK server is listening."""
    def __init__(
        self,
        *,
        sdk_server_port: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_sdk_server_port", b"_sdk_server_port", "sdk_server_port", b"sdk_server_port"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_sdk_server_port", b"_sdk_server_port", "sdk_server_port", b"sdk_server_port"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_sdk_server_port", b"_sdk_server_port"]) -> typing_extensions.Literal["sdk_server_port"] | None: ...

global___SdkServerReadyRequest = SdkServerReadyRequest

@typing_extensions.final
class SdkServerReadyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___SdkServerReadyResponse = SdkServerReadyResponse
