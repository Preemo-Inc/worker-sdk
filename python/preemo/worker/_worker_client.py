from typing import Callable, Optional

from google.protobuf.struct_pb2 import NULL_VALUE

from preemo.gen.endpoints.check_function_pb2 import CheckFunctionRequest
from preemo.gen.endpoints.execute_function_pb2 import ExecuteFunctionRequest
from preemo.gen.endpoints.register_function_pb2 import RegisterFunctionRequest
from preemo.gen.models.registered_function_pb2 import RegisteredFunction
from preemo.gen.models.value_pb2 import Value
from preemo.worker._artifact_manager import (
    ArtifactId,
    ArtifactManager,
    IArtifactManager,
)
from preemo.worker._function_registry import FunctionRegistry
from preemo.worker._messaging_client import IMessagingClient


class Function:
    def __init__(
        self,
        *,
        artifact_manager: IArtifactManager,
        messaging_client: IMessagingClient,
        name: str,
        namespace: Optional[str],
    ) -> None:
        self._artifact_manager = artifact_manager
        self._client = messaging_client
        self.name = name
        self.namespace = namespace

        self._ensure_function_is_registered()

    def _ensure_function_is_registered(self) -> None:
        # check_function raises an error if the function is not found
        self._client.check_function(
            CheckFunctionRequest(
                registered_function=RegisteredFunction(
                    name=self.name, namespace=self.namespace
                )
            )
        )

    def __call__(self, params: Optional[str] = None) -> Optional[str]:
        if params is None:
            function_parameter = Value(null_value=NULL_VALUE)
        else:
            artifact_id = self._artifact_manager.create_artifact(params)
            function_parameter = Value(artifact_id=artifact_id.value)

        response = self._client.execute_function(
            ExecuteFunctionRequest(
                function_to_execute=RegisteredFunction(
                    name=self.name, namespace=self.namespace
                ),
                function_parameters_by_index={0: function_parameter},
            )
        )

        function_result = response.function_results_by_index[0]

        match function_result.WhichOneof("kind"):
            case "null_value":
                return None
            case "artifact_id":
                return self._artifact_manager.get_artifact(
                    ArtifactId(value=function_result.artifact_id)
                )
            case _:
                raise Exception(
                    f"received unexpected function_result: {function_result}"
                )


class WorkerClient:
    def __init__(self, *, messaging_client: IMessagingClient) -> None:
        self._client = messaging_client
        # TODO(adrian@preemo.io, 03/15/2023): figure out if artifact manager should be passed in?
        # needs to depend on the same messaging client though
        self._artifact_manager = ArtifactManager(messaging_client=messaging_client)
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
        return Function(
            artifact_manager=self._artifact_manager,
            messaging_client=self._client,
            name=name,
            namespace=namespace,
        )

    def parallelize(self, function: Function, params: list[str]) -> list[Optional[str]]:
        if len(params) == 0:
            return []

        # TODO(adrian@preemo.io, 03/08/2023): should batch?

        artifact_ids = self._artifact_manager.create_artifacts(params)
        function_parameters_by_index = {
            i: Value(artifact_id=artifact_id.value)
            for i, artifact_id in enumerate(artifact_ids)
        }

        response = self._client.execute_function(
            ExecuteFunctionRequest(
                function_to_execute=RegisteredFunction(
                    name=function.name, namespace=function.namespace
                ),
                function_parameters_by_index=function_parameters_by_index,
            )
        )

        results: list[Optional[str]] = []
        # TODO(adrian@preemo.io, 03/15/2023): should download results in parallel
        # or just return a handle that allows the user to download
        for _, function_result in sorted(
            response.function_results_by_index.items(), key=lambda x: x[0]
        ):
            match function_result.WhichOneof("kind"):
                case "null_value":
                    results.append(None)
                case "artifact_id":
                    results.append(
                        self._artifact_manager.get_artifact(
                            ArtifactId(value=function_result.artifact_id)
                        )
                    )
                case _:
                    raise Exception(
                        f"received unexpected function_result: {function_result}"
                    )

        return results
