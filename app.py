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

if __name__ == '__main__':
    app.run(debug=True)
