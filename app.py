import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Store location data
locations = []

@app.route('/')
def home():
    return "Hello, visit /location to send your location."

@app.route('/location', methods=['POST'])
def store_location():
    data = request.get_json()  # Parse the incoming JSON data
    print(data)  # Print data to the console for debugging

    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if latitude is None or longitude is None:
        return jsonify({"message": "Missing latitude or longitude"}), 400

    # Add the location to the list
    locations.append({"latitude": latitude, "longitude": longitude})
    return jsonify({"message": "Location data received successfully!"}), 200

@app.route('/locations', methods=['GET'])
def get_locations():
    return jsonify(locations), 200

if __name__ == '__main__':
    # Use a specific port (10000) to match the deployment configuration
    app.run(debug=True, host='0.0.0.0', port=10000)
