"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ArtifactType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ArtifactTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ArtifactType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ARTIFACT_TYPE_UNSPECIFIED: _ArtifactType.ValueType  # 0
    ARTIFACT_TYPE_PARAMS: _ArtifactType.ValueType  # 1
    ARTIFACT_TYPE_RESULT: _ArtifactType.ValueType  # 2

class ArtifactType(_ArtifactType, metaclass=_ArtifactTypeEnumTypeWrapper): ...

ARTIFACT_TYPE_UNSPECIFIED: ArtifactType.ValueType  # 0
ARTIFACT_TYPE_PARAMS: ArtifactType.ValueType  # 1
ARTIFACT_TYPE_RESULT: ArtifactType.ValueType  # 2
global___ArtifactType = ArtifactType