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
    longitude = data
