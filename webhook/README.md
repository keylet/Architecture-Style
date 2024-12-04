## Requirements  
- Python 3.7 or higher  
- Flask (install using `pip install -r requirements.txt`)  

## Run the Project  
1. Clone the repository or copy the files.  
2. Install dependencies with `pip install -r requirements.txt`.  
3. Run the file `app.py` with `python app.py`.  
4. The WebHook endpoint will be available at `http://127.0.0.1:5001/webhook`.  

## How It Works  
- The WebHook listener waits for HTTP POST requests at the `/webhook` endpoint.  
- When data is received, it logs the information and responds with a success message.  

## Testing the WebHook  
- Use a tool like **Postman** or `curl` to send a POST request to the endpoint:  
  ```bash
  curl -X POST http://127.0.0.1:5001/webhook \
       -H "Content-Type: application/json" \
       -d '{"event": "test_event", "data": "sample data"}'
