from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    ip_address = request.remote_addr  # Get the IP address of the user
    user_agent = request.user_agent.string  # Get the User-Agent string (device info)
    
    print(f"IP Address: {ip_address}")
    print(f"User-Agent: {user_agent}")
    
    return jsonify({
        "message": "Hello, visit /location to send your location.",
        "ip": ip_address,
        "device": user_agent
    }), 200

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Get the port from the environment, default to 5000
    app.run(host='0.0.0.0', port=port)  # Bind to 0.0.0.0 for external access
