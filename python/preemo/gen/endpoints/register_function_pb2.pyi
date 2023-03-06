from models import registered_function_pb2 as _registered_function_pb2
from models import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterFunctionRequest(_message.Message):
    __slots__ = ["function_to_register"]
    FUNCTION_TO_REGISTER_FIELD_NUMBER: _ClassVar[int]
    function_to_register: _registered_function_pb2.RegisteredFunction
    def __init__(self, function_to_register: _Optional[_Union[_registered_function_pb2.RegisteredFunction, _Mapping]] = ...) -> None: ...

class RegisterFunctionResponse(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: _status_pb2.Status
    def __init__(self, status: _Optional[_Union[_status_pb2.Status, str]] = ..., message: _Optional[str] = ...) -> None: ...
