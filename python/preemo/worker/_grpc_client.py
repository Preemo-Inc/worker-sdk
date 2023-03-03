import grpc

import preemo.gen.worker_service_pb2


def run() -> None:
    # TODO(adrian@preemo.io, 03/03/2023): consider using secure_channel
    with grpc.insecure_channel("localhost:50051") as channel:
        # preemo.gen.worker_service_pb2.
        # WorkerService(channel)
        # stub = helloworld_pb2_grpc.GreeterStub(channel)
        # response = stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
