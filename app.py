from flask import Flask, request, jsonify

app = Flask(__name__)

# Store location data
locations = []

@app.route('/')
def home():
    return "Hello, visit /location to send your location."

@app.route('/location', methods=['POST'])
def store_location():
<<<<<<< HEAD
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
=======
    data = request.get_json()  # Parse the incoming JSON data
    print(data)  # Print data to the console for debugging

    latitude = data.get('latitude')
    longitude = data.get('longitude')
>>>>>>> 2638cbe (Initial commit with app.py, requirements.txt, and templates)

    if latitude and longitude:
        locations.append({"latitude": latitude, "longitude": longitude})
        return jsonify({"message": "Location data received successfully!"}), 200
    else:
        return jsonify({"message": "Location data is missing!"}), 400

@app.route('/locations', methods=['GET'])
def get_locations():
    return jsonify(locations), 200

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True, host='0.0.0.0', port=5000)  # Fixed closing parenthesis
=======
    app.run(debug=True)
>>>>>>> 2638cbe (Initial commit with app.py, requirements.txt, and templates)
