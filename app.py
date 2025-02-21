import os
from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Store location data and logs in memory
locations = []

# Load logs from a file if it exists
def load_logs():
    if os.path.exists('logs.json'):
        with open('logs.json', 'r') as f:
            return json.load(f)
    return []

logs = load_logs()

@app.route('/')
def home():
    # Capture user details like IP and device
    user_ip = request.remote_addr
    user_device = request.user_agent.string
    log_entry = {"ip": user_ip, "device": user_device, "message": "Hello, visit /location to send your location."}
    logs.append(log_entry)
    
    # Save the log to a file
    with open('logs.json', 'w') as f:
        json.dump(logs, f)

    # Return an HTML page with animation and user details
    return render_template('index.html', log_entry=log_entry)

@app.route('/location', methods=['POST'])
def store_location():
    data = request.get_json()  # Parse the incoming JSON data
    print(data)  # Print data to the console for debugging

    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if latitude and longitude:
        locations.append({"latitude": latitude, "longitude": longitude})
        return jsonify({"message": "Location data received successfully!"}), 200
    else:
        return jsonify({"message": "Location data is missing!"}), 400

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logs), 200

if __name__ == '__main__':
    app.run(debug=True)
