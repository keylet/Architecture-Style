## Requirements  
- Python 3.7 or higher  
- Install dependencies: `pip install -r requirements.txt`  

## Setup  
1. Clone the repository or copy the files.  
2. Generate the gRPC code using:  
   ```bash
   python -m grpc_tools.protoc -I ./protos --python_out=. --grpc_python_out=. ./protos/service.proto
