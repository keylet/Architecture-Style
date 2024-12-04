import grpc
import protos.service_pb2 as service_pb2
import protos.service_pb2_grpc as service_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.ItemServiceStub(channel)
        response = stub.GetItem(service_pb2.ItemRequest(id=1))
        print(f"Received: ID={response.id}, Name={response.name}")

if __name__ == "__main__":
    run()
