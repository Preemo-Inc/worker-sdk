# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from endpoints import execute_function_pb2 as endpoints_dot_execute__function__pb2
from endpoints import terminate_pb2 as endpoints_dot_terminate__pb2


class SDKServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ExecuteFunction = channel.unary_unary(
                '/services.SDKService/ExecuteFunction',
                request_serializer=endpoints_dot_execute__function__pb2.ExecuteFunctionRequest.SerializeToString,
                response_deserializer=endpoints_dot_execute__function__pb2.ExecuteFunctionResponse.FromString,
                )
        self.Terminate = channel.unary_unary(
                '/services.SDKService/Terminate',
                request_serializer=endpoints_dot_terminate__pb2.TerminateRequest.SerializeToString,
                response_deserializer=endpoints_dot_terminate__pb2.TerminateResponse.FromString,
                )


class SDKServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ExecuteFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Terminate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SDKServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ExecuteFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteFunction,
                    request_deserializer=endpoints_dot_execute__function__pb2.ExecuteFunctionRequest.FromString,
                    response_serializer=endpoints_dot_execute__function__pb2.ExecuteFunctionResponse.SerializeToString,
            ),
            'Terminate': grpc.unary_unary_rpc_method_handler(
                    servicer.Terminate,
                    request_deserializer=endpoints_dot_terminate__pb2.TerminateRequest.FromString,
                    response_serializer=endpoints_dot_terminate__pb2.TerminateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'services.SDKService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SDKService(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/services.SDKService/ExecuteFunction',
            endpoints_dot_execute__function__pb2.ExecuteFunctionRequest.SerializeToString,
            endpoints_dot_execute__function__pb2.ExecuteFunctionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Terminate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.SDKService/Terminate',
            endpoints_dot_terminate__pb2.TerminateRequest.SerializeToString,
            endpoints_dot_terminate__pb2.TerminateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)