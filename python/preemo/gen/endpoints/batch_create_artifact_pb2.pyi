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
class CreateArtifactConfig(google.protobuf.message.Message):
    """This config is included for potential future use.
    In the future it may include part count, expiration, or other metadata.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___CreateArtifactConfig = CreateArtifactConfig

@typing_extensions.final
class BatchCreateArtifactRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ConfigsByIndexEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___CreateArtifactConfig: ...
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: global___CreateArtifactConfig | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    CONFIGS_BY_INDEX_FIELD_NUMBER: builtins.int
    @property
    def configs_by_index(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___CreateArtifactConfig]:
        """This field is a map instead of an array to avoid depending on the
        response array being in the same order as the request array.
        """
    def __init__(
        self,
        *,
        configs_by_index: collections.abc.Mapping[builtins.int, global___CreateArtifactConfig] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["configs_by_index", b"configs_by_index"]) -> None: ...

global___BatchCreateArtifactRequest = BatchCreateArtifactRequest

@typing_extensions.final
class CreateArtifactResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ARTIFACT_ID_FIELD_NUMBER: builtins.int
    PART_SIZE_THRESHOLD_FIELD_NUMBER: builtins.int
    artifact_id: builtins.str
    """Required field for a unique identifier of an artifact."""
    part_size_threshold: builtins.int
    """Required field indicating the precise number of bytes a part should
    reach before creating the next part.
    """
    def __init__(
        self,
        *,
        artifact_id: builtins.str | None = ...,
        part_size_threshold: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_artifact_id", b"_artifact_id", "_part_size_threshold", b"_part_size_threshold", "artifact_id", b"artifact_id", "part_size_threshold", b"part_size_threshold"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_artifact_id", b"_artifact_id", "_part_size_threshold", b"_part_size_threshold", "artifact_id", b"artifact_id", "part_size_threshold", b"part_size_threshold"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_artifact_id", b"_artifact_id"]) -> typing_extensions.Literal["artifact_id"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_part_size_threshold", b"_part_size_threshold"]) -> typing_extensions.Literal["part_size_threshold"] | None: ...

global___CreateArtifactResult = CreateArtifactResult

@typing_extensions.final
class BatchCreateArtifactResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ResultsByIndexEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___CreateArtifactResult: ...
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: global___CreateArtifactResult | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    RESULTS_BY_INDEX_FIELD_NUMBER: builtins.int
    @property
    def results_by_index(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___CreateArtifactResult]: ...
    def __init__(
        self,
        *,
        results_by_index: collections.abc.Mapping[builtins.int, global___CreateArtifactResult] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["results_by_index", b"results_by_index"]) -> None: ...

global___BatchCreateArtifactResponse = BatchCreateArtifactResponse
