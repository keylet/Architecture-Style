from concurrent import futures
import grpc
import protos.service_pb2 as service_pb2
import protos.service_pb2_grpc as service_pb2_grpc

class ItemService(service_pb2_grpc.ItemServiceServicer):
    def GetItem(self, request, context):
        # Example data
        items = {1: "Item 1", 2: "Item 2"}
        item_name = items.get(request.id, "Item not found")
        return service_pb2.ItemResponse(id=request.id, name=item_name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ItemServiceServicer_to_server(ItemService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server is running on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
