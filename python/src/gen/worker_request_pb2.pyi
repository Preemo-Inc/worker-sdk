from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterFunctionsRequest(_message.Message):
    __slots__ = ["functions_to_register"]
    FUNCTIONS_TO_REGISTER_FIELD_NUMBER: _ClassVar[int]
    functions_to_register: _containers.RepeatedCompositeFieldContainer[RegisteredFunction]
    def __init__(self, functions_to_register: _Optional[_Iterable[_Union[RegisteredFunction, _Mapping]]] = ...) -> None: ...

class RegisteredFunction(_message.Message):
    __slots__ = ["name", "namespace"]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ...) -> None: ...

class WorkerRequest(_message.Message):
    __slots__ = ["register_functions"]
    REGISTER_FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    register_functions: RegisterFunctionsRequest
    def __init__(self, register_functions: _Optional[_Union[RegisterFunctionsRequest, _Mapping]] = ...) -> None: ...
