from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/location', methods=['POST'])
def store_location():
    data = request.get_json()  # Get the JSON data sent in the request
    ip_address = request.remote_addr  # Get the IP address of the user
    user_agent = request.user_agent.string  # Get the User-Agent string (device info)
    
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    
    if latitude and longitude:
        # You can save or process the data here
        print(f"Location data: Latitude={latitude}, Longitude={longitude}")
        print(f"IP Address: {ip_address}")
        print(f"User-Agent: {user_agent}")
        
        return jsonify({"message": "Location data received", "ip": ip_address, "device": user_agent}), 200
    else:
        return jsonify({"message": "Location data is missing!"}), 400

if __name__ == '__main__':
    app.run(debug=True)
