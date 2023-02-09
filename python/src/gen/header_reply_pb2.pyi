from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
HEADER_STATUS_OK: HeaderStatus
HEADER_STATUS_UNSPECIFIED: HeaderStatus

class HeaderReply(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: HeaderStatus
    def __init__(self, status: _Optional[_Union[HeaderStatus, str]] = ..., message: _Optional[str] = ...) -> None: ...

class HeaderStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
