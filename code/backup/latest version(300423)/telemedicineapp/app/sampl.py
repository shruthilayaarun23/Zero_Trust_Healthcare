from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/combined_data', methods=['GET'])
def get_combined_data():
    # Make API calls
    response1 = requests.get("https://localhost:5000/patient_imaging/getAllPatients")
    

    # Extract data from responses
    data1 = response1.json()
    

    # Combine data into a single JSON object
    combined_data = {
        "data1": data1,

    }

    # Convert JSON object to string
    json_string = json.dumps(combined_data)

    # Return JSON response
    return jsonify(json_string)

if __name__ == '__main__':
    app.run()
