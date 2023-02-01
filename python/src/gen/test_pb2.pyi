from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TestMessage(_message.Message):
    __slots__ = ["page_number", "query", "result_per_page"]
    PAGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    RESULT_PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    page_number: int
    query: str
    result_per_page: int
    def __init__(self, query: _Optional[str] = ..., page_number: _Optional[int] = ..., result_per_page: _Optional[int] = ...) -> None: ...
