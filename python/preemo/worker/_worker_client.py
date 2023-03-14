from typing import Callable, Optional

from preemo.gen.endpoints.batch_create_artifact_part_pb2 import (
    BatchCreateArtifactPartRequest,
    CreateArtifactPartConfig,
    CreateArtifactPartConfigMetadata,
)
from preemo.gen.endpoints.batch_create_artifact_pb2 import (
    BatchCreateArtifactRequest,
    CreateArtifactConfig,
)
from preemo.gen.endpoints.check_function_pb2 import CheckFunctionRequest
from preemo.gen.endpoints.register_function_pb2 import RegisterFunctionRequest
from preemo.gen.models.registered_function_pb2 import RegisteredFunction
from preemo.worker._function_registry import FunctionRegistry
from preemo.worker._messaging_client import IMessagingClient


class Function:
    def __init__(
        self, *, messaging_client: IMessagingClient, name: str, namespace: Optional[str]
    ) -> None:
        self._client = messaging_client
        self._name = name
        self._namespace = namespace

        self._ensure_function_is_registered()

    def _ensure_function_is_registered(self) -> None:
        # check_function raises an error if the function is not found
        self._client.check_function(
            CheckFunctionRequest(
                registered_function=RegisteredFunction(
                    name=self._name, namespace=self._namespace
                )
            )
        )

    def _create_single_artifact(self) -> str:
        response = self._client.batch_create_artifact(
            BatchCreateArtifactRequest(configs_by_index={0: CreateArtifactConfig()})
        )

        if len(response.results_by_index) != 1:
            raise ValueError("expected exactly one artifact result")

        if 0 not in response.results_by_index:
            raise ValueError("expected 0 to be a key in results_by_index")

        result = response.results_by_index[0]
        if not result.HasField("artifact_id"):
            raise ValueError("expected create artifact result to have artifact_id")

        return result.artifact_id

    def _create_single_part_for_artifact(
        self, artifact_id: str, *, part_number: int
    ) -> str:
        response = self._client.batch_create_artifact_part(
            BatchCreateArtifactPartRequest(
                configs_by_artifact_id={
                    artifact_id: CreateArtifactPartConfig(
                        metadatas_by_part_number={
                            part_number: CreateArtifactPartConfigMetadata()
                        }
                    )
                }
            )
        )

        if len(response.results_by_artifact_id) != 1:
            raise ValueError("expected exactly one artifact part result")

        if artifact_id not in response.results_by_artifact_id:
            raise ValueError(
                "expected artifact_id to be a key in results_by_artifact_id"
            )

        result = response.results_by_artifact_id[artifact_id]

        if len(result.metadatas_by_part_number) != 1:
            raise ValueError("expected exactly one artifact part result metadata")

        if part_number not in result.metadatas_by_part_number:
            raise ValueError(
                "expected part_number to be a key in metadatas_by_part_number"
            )

        metadata = result.metadatas_by_part_number[part_number]
        if not metadata.HasField("upload_signed_url"):
            raise ValueError(
                "expected create artifact part result metadata to have upload_signed_url"
            )

        return metadata.upload_signed_url

    def __call__(self, params: Optional[str] = None) -> Optional[str]:
        if params is not None:
            artifact_id = self._create_single_artifact()
            upload_signed_url = self._create_single_part_for_artifact(
                artifact_id, part_number=1
            )

            # TODO(adrian@preemo.io, 03/08/2023): upload params
            # and decide size for multipart upload
            # and decide best way to get size of params len() for now, maybe sys.getsizeof at some point?
            pass

        # TODO(adrian@preemo.io, 03/08/2023):
        # send request to worker to execute request
        # wait for response and return it
        raise Exception("not yet implemented")


class WorkerClient:
    def __init__(self, *, messaging_client: IMessagingClient) -> None:
        self._client = messaging_client
        self._function_registry = FunctionRegistry()

    def register(
        self,
        outer_function: Optional[Callable] = None,
        *,
        name: Optional[str] = None,
        namespace: Optional[str] = None,
    ) -> Callable:
        def decorator(function: Callable) -> Callable:
            if name is None:
                function_name = function.__name__
            else:
                function_name = name

            self._function_registry.register_function(
                function, name=function_name, namespace=namespace
            )

            self._client.register_function(
                RegisterFunctionRequest(
                    function_to_register=RegisteredFunction(
                        name=function_name, namespace=namespace
                    )
                )
            )

            return function

        if outer_function is None:
            return decorator

        return decorator(outer_function)

    def get_function(self, name: str, *, namespace: Optional[str] = None) -> Function:
        return Function(messaging_client=self._client, name=name, namespace=namespace)

    def parallelize(self, function: Function, params: list[str]) -> list[Optional[str]]:
        if len(params) == 0:
            return []

        # TODO(adrian@preemo.io, 03/08/2023):
        # ask worker to parallelize function with params
        raise Exception("not yet implemented")
