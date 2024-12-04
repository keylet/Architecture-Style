from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to receive WebHook events
@app.route('/webhook', methods=['POST'])
def webhook():
    # Extract data from the request
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data received"}), 400

    # Process the received data (example: log it)
    print("Received WebHook data:", data)

    # Send a response to acknowledge receipt
    return jsonify({"message": "WebHook received successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
