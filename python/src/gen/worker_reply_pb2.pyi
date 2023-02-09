from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
WORKER_STATUS_FAILURE: WorkerStatus
WORKER_STATUS_SUCCESS: WorkerStatus
WORKER_STATUS_UNSPECIFIED: WorkerStatus

class RegisterFunctionReply(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: WorkerStatus
    def __init__(self, status: _Optional[_Union[WorkerStatus, str]] = ..., message: _Optional[str] = ...) -> None: ...

class WorkerReply(_message.Message):
    __slots__ = ["register_function"]
    REGISTER_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    register_function: RegisterFunctionReply
    def __init__(self, register_function: _Optional[_Union[RegisterFunctionReply, _Mapping]] = ...) -> None: ...

class WorkerStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
