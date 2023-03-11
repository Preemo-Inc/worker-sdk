# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from endpoints import batch_create_artifact_part_pb2 as endpoints_dot_batch__create__artifact__part__pb2
from endpoints import batch_create_artifact_pb2 as endpoints_dot_batch__create__artifact__pb2
from endpoints import batch_get_artifact_part_pb2 as endpoints_dot_batch__get__artifact__part__pb2
from endpoints import batch_get_artifact_pb2 as endpoints_dot_batch__get__artifact__pb2
from endpoints import execute_function_pb2 as endpoints_dot_execute__function__pb2
from endpoints import header_pb2 as endpoints_dot_header__pb2
from endpoints import register_function_pb2 as endpoints_dot_register__function__pb2


class WorkerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BatchCreateArtifact = channel.unary_unary(
                '/services.WorkerService/BatchCreateArtifact',
                request_serializer=endpoints_dot_batch__create__artifact__pb2.BatchCreateArtifactRequest.SerializeToString,
                response_deserializer=endpoints_dot_batch__create__artifact__pb2.BatchCreateArtifactResponse.FromString,
                )
        self.BatchCreateArtifactPart = channel.unary_unary(
                '/services.WorkerService/BatchCreateArtifactPart',
                request_serializer=endpoints_dot_batch__create__artifact__part__pb2.BatchCreateArtifactPartRequest.SerializeToString,
                response_deserializer=endpoints_dot_batch__create__artifact__part__pb2.BatchCreateArtifactPartResponse.FromString,
                )
        self.BatchGetArtifact = channel.unary_unary(
                '/services.WorkerService/BatchGetArtifact',
                request_serializer=endpoints_dot_batch__get__artifact__pb2.BatchGetArtifactRequest.SerializeToString,
                response_deserializer=endpoints_dot_batch__get__artifact__pb2.BatchGetArtifactResponse.FromString,
                )
        self.BatchGetArtifactPart = channel.unary_unary(
                '/services.WorkerService/BatchGetArtifactPart',
                request_serializer=endpoints_dot_batch__get__artifact__part__pb2.BatchGetArtifactPartRequest.SerializeToString,
                response_deserializer=endpoints_dot_batch__get__artifact__part__pb2.BatchGetArtifactPartResponse.FromString,
                )
        self.ExecuteFunction = channel.unary_unary(
                '/services.WorkerService/ExecuteFunction',
                request_serializer=endpoints_dot_execute__function__pb2.ExecuteFunctionRequest.SerializeToString,
                response_deserializer=endpoints_dot_execute__function__pb2.ExecuteFunctionResponse.FromString,
                )
        self.Initiate = channel.unary_unary(
                '/services.WorkerService/Initiate',
                request_serializer=endpoints_dot_header__pb2.HeaderRequest.SerializeToString,
                response_deserializer=endpoints_dot_header__pb2.HeaderResponse.FromString,
                )
        self.RegisterFunction = channel.unary_unary(
                '/services.WorkerService/RegisterFunction',
                request_serializer=endpoints_dot_register__function__pb2.RegisterFunctionRequest.SerializeToString,
                response_deserializer=endpoints_dot_register__function__pb2.RegisterFunctionResponse.FromString,
                )


class WorkerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BatchCreateArtifact(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchCreateArtifactPart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetArtifact(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetArtifactPart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecuteFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Initiate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BatchCreateArtifact': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchCreateArtifact,
                    request_deserializer=endpoints_dot_batch__create__artifact__pb2.BatchCreateArtifactRequest.FromString,
                    response_serializer=endpoints_dot_batch__create__artifact__pb2.BatchCreateArtifactResponse.SerializeToString,
            ),
            'BatchCreateArtifactPart': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchCreateArtifactPart,
                    request_deserializer=endpoints_dot_batch__create__artifact__part__pb2.BatchCreateArtifactPartRequest.FromString,
                    response_serializer=endpoints_dot_batch__create__artifact__part__pb2.BatchCreateArtifactPartResponse.SerializeToString,
            ),
            'BatchGetArtifact': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetArtifact,
                    request_deserializer=endpoints_dot_batch__get__artifact__pb2.BatchGetArtifactRequest.FromString,
                    response_serializer=endpoints_dot_batch__get__artifact__pb2.BatchGetArtifactResponse.SerializeToString,
            ),
            'BatchGetArtifactPart': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetArtifactPart,
                    request_deserializer=endpoints_dot_batch__get__artifact__part__pb2.BatchGetArtifactPartRequest.FromString,
                    response_serializer=endpoints_dot_batch__get__artifact__part__pb2.BatchGetArtifactPartResponse.SerializeToString,
            ),
            'ExecuteFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteFunction,
                    request_deserializer=endpoints_dot_execute__function__pb2.ExecuteFunctionRequest.FromString,
                    response_serializer=endpoints_dot_execute__function__pb2.ExecuteFunctionResponse.SerializeToString,
            ),
            'Initiate': grpc.unary_unary_rpc_method_handler(
                    servicer.Initiate,
                    request_deserializer=endpoints_dot_header__pb2.HeaderRequest.FromString,
                    response_serializer=endpoints_dot_header__pb2.HeaderResponse.SerializeToString,
            ),
            'RegisterFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterFunction,
                    request_deserializer=endpoints_dot_register__function__pb2.RegisterFunctionRequest.FromString,
                    response_serializer=endpoints_dot_register__function__pb2.RegisterFunctionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'services.WorkerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WorkerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BatchCreateArtifact(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.WorkerService/BatchCreateArtifact',
            endpoints_dot_batch__create__artifact__pb2.BatchCreateArtifactRequest.SerializeToString,
            endpoints_dot_batch__create__artifact__pb2.BatchCreateArtifactResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchCreateArtifactPart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.WorkerService/BatchCreateArtifactPart',
            endpoints_dot_batch__create__artifact__part__pb2.BatchCreateArtifactPartRequest.SerializeToString,
            endpoints_dot_batch__create__artifact__part__pb2.BatchCreateArtifactPartResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchGetArtifact(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.WorkerService/BatchGetArtifact',
            endpoints_dot_batch__get__artifact__pb2.BatchGetArtifactRequest.SerializeToString,
            endpoints_dot_batch__get__artifact__pb2.BatchGetArtifactResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchGetArtifactPart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.WorkerService/BatchGetArtifactPart',
            endpoints_dot_batch__get__artifact__part__pb2.BatchGetArtifactPartRequest.SerializeToString,
            endpoints_dot_batch__get__artifact__part__pb2.BatchGetArtifactPartResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExecuteFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.WorkerService/ExecuteFunction',
            endpoints_dot_execute__function__pb2.ExecuteFunctionRequest.SerializeToString,
            endpoints_dot_execute__function__pb2.ExecuteFunctionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Initiate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.WorkerService/Initiate',
            endpoints_dot_header__pb2.HeaderRequest.SerializeToString,
            endpoints_dot_header__pb2.HeaderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.WorkerService/RegisterFunction',
            endpoints_dot_register__function__pb2.RegisterFunctionRequest.SerializeToString,
            endpoints_dot_register__function__pb2.RegisterFunctionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
