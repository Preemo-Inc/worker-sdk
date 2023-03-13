"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import preemo.gen.endpoints.batch_create_artifact_part_pb2
import preemo.gen.endpoints.batch_create_artifact_pb2
import preemo.gen.endpoints.batch_get_artifact_part_pb2
import preemo.gen.endpoints.batch_get_artifact_pb2
import preemo.gen.endpoints.check_function_pb2
import preemo.gen.endpoints.execute_function_pb2
import preemo.gen.endpoints.header_pb2
import preemo.gen.endpoints.register_function_pb2
import grpc

class WorkerServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    BatchCreateArtifact: grpc.UnaryUnaryMultiCallable[
        preemo.gen.endpoints.batch_create_artifact_pb2.BatchCreateArtifactRequest,
        preemo.gen.endpoints.batch_create_artifact_pb2.BatchCreateArtifactResponse,
    ]
    BatchCreateArtifactPart: grpc.UnaryUnaryMultiCallable[
        preemo.gen.endpoints.batch_create_artifact_part_pb2.BatchCreateArtifactPartRequest,
        preemo.gen.endpoints.batch_create_artifact_part_pb2.BatchCreateArtifactPartResponse,
    ]
    BatchGetArtifact: grpc.UnaryUnaryMultiCallable[
        preemo.gen.endpoints.batch_get_artifact_pb2.BatchGetArtifactRequest,
        preemo.gen.endpoints.batch_get_artifact_pb2.BatchGetArtifactResponse,
    ]
    BatchGetArtifactPart: grpc.UnaryUnaryMultiCallable[
        preemo.gen.endpoints.batch_get_artifact_part_pb2.BatchGetArtifactPartRequest,
        preemo.gen.endpoints.batch_get_artifact_part_pb2.BatchGetArtifactPartResponse,
    ]
    CheckFunction: grpc.UnaryUnaryMultiCallable[
        preemo.gen.endpoints.check_function_pb2.CheckFunctionRequest,
        preemo.gen.endpoints.check_function_pb2.CheckFunctionResponse,
    ]
    ExecuteFunction: grpc.UnaryUnaryMultiCallable[
        preemo.gen.endpoints.execute_function_pb2.ExecuteFunctionRequest,
        preemo.gen.endpoints.execute_function_pb2.ExecuteFunctionResponse,
    ]
    Initiate: grpc.UnaryUnaryMultiCallable[
        preemo.gen.endpoints.header_pb2.HeaderRequest,
        preemo.gen.endpoints.header_pb2.HeaderResponse,
    ]
    RegisterFunction: grpc.UnaryUnaryMultiCallable[
        preemo.gen.endpoints.register_function_pb2.RegisterFunctionRequest,
        preemo.gen.endpoints.register_function_pb2.RegisterFunctionResponse,
    ]

class WorkerServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def BatchCreateArtifact(
        self,
        request: preemo.gen.endpoints.batch_create_artifact_pb2.BatchCreateArtifactRequest,
        context: grpc.ServicerContext,
    ) -> preemo.gen.endpoints.batch_create_artifact_pb2.BatchCreateArtifactResponse: ...
    @abc.abstractmethod
    def BatchCreateArtifactPart(
        self,
        request: preemo.gen.endpoints.batch_create_artifact_part_pb2.BatchCreateArtifactPartRequest,
        context: grpc.ServicerContext,
    ) -> preemo.gen.endpoints.batch_create_artifact_part_pb2.BatchCreateArtifactPartResponse: ...
    @abc.abstractmethod
    def BatchGetArtifact(
        self,
        request: preemo.gen.endpoints.batch_get_artifact_pb2.BatchGetArtifactRequest,
        context: grpc.ServicerContext,
    ) -> preemo.gen.endpoints.batch_get_artifact_pb2.BatchGetArtifactResponse: ...
    @abc.abstractmethod
    def BatchGetArtifactPart(
        self,
        request: preemo.gen.endpoints.batch_get_artifact_part_pb2.BatchGetArtifactPartRequest,
        context: grpc.ServicerContext,
    ) -> preemo.gen.endpoints.batch_get_artifact_part_pb2.BatchGetArtifactPartResponse: ...
    @abc.abstractmethod
    def CheckFunction(
        self,
        request: preemo.gen.endpoints.check_function_pb2.CheckFunctionRequest,
        context: grpc.ServicerContext,
    ) -> preemo.gen.endpoints.check_function_pb2.CheckFunctionResponse: ...
    @abc.abstractmethod
    def ExecuteFunction(
        self,
        request: preemo.gen.endpoints.execute_function_pb2.ExecuteFunctionRequest,
        context: grpc.ServicerContext,
    ) -> preemo.gen.endpoints.execute_function_pb2.ExecuteFunctionResponse: ...
    @abc.abstractmethod
    def Initiate(
        self,
        request: preemo.gen.endpoints.header_pb2.HeaderRequest,
        context: grpc.ServicerContext,
    ) -> preemo.gen.endpoints.header_pb2.HeaderResponse: ...
    @abc.abstractmethod
    def RegisterFunction(
        self,
        request: preemo.gen.endpoints.register_function_pb2.RegisterFunctionRequest,
        context: grpc.ServicerContext,
    ) -> preemo.gen.endpoints.register_function_pb2.RegisterFunctionResponse: ...

def add_WorkerServiceServicer_to_server(servicer: WorkerServiceServicer, server: grpc.Server) -> None: ...
