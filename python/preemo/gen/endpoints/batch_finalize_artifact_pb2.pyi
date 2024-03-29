"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class FinalizeArtifactConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOTAL_SIZE_FIELD_NUMBER: builtins.int
    PART_COUNT_FIELD_NUMBER: builtins.int
    total_size: builtins.int
    """Required field representing the size in bytes of the combined artifact parts."""
    part_count: builtins.int
    """Required field indicating the number of parts that were written to."""
    def __init__(
        self,
        *,
        total_size: builtins.int | None = ...,
        part_count: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_part_count", b"_part_count", "_total_size", b"_total_size", "part_count", b"part_count", "total_size", b"total_size"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_part_count", b"_part_count", "_total_size", b"_total_size", "part_count", b"part_count", "total_size", b"total_size"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_part_count", b"_part_count"]) -> typing_extensions.Literal["part_count"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_total_size", b"_total_size"]) -> typing_extensions.Literal["total_size"] | None: ...

global___FinalizeArtifactConfig = FinalizeArtifactConfig

@typing_extensions.final
class BatchFinalizeArtifactRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ConfigsByArtifactIdEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___FinalizeArtifactConfig: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___FinalizeArtifactConfig | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    CONFIGS_BY_ARTIFACT_ID_FIELD_NUMBER: builtins.int
    @property
    def configs_by_artifact_id(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___FinalizeArtifactConfig]: ...
    def __init__(
        self,
        *,
        configs_by_artifact_id: collections.abc.Mapping[builtins.str, global___FinalizeArtifactConfig] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["configs_by_artifact_id", b"configs_by_artifact_id"]) -> None: ...

global___BatchFinalizeArtifactRequest = BatchFinalizeArtifactRequest

@typing_extensions.final
class FinalizeArtifactResult(google.protobuf.message.Message):
    """This message is included for potential future use."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___FinalizeArtifactResult = FinalizeArtifactResult

@typing_extensions.final
class BatchFinalizeArtifactResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ResultsByArtifactIdEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___FinalizeArtifactResult: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___FinalizeArtifactResult | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    RESULTS_BY_ARTIFACT_ID_FIELD_NUMBER: builtins.int
    @property
    def results_by_artifact_id(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___FinalizeArtifactResult]: ...
    def __init__(
        self,
        *,
        results_by_artifact_id: collections.abc.Mapping[builtins.str, global___FinalizeArtifactResult] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["results_by_artifact_id", b"results_by_artifact_id"]) -> None: ...

global___BatchFinalizeArtifactResponse = BatchFinalizeArtifactResponse
