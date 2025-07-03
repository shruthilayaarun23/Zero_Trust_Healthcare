from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/combined_data', methods=['GET'])
def get_combined_data():
    # Make API calls
    response1 = requests.get("https://127.0.0.1.dw.sslip.io/dose-watch/read")
    response2 = requests.get("https://127.0.0.1.pd.sslip.io/patient-details/read")
    response3 = requests.get("https://127.0.0.1.pi.sslip.io/patient_imaging/getAllPatients")

    # Extract data from responses
    data1 = response1.json()
    data2 = response2.json()
    data3 = response3.json()

    # Combine data into a single JSON object
    combined_data = {
        "data1": data1,
        "data2": data2,
        "data3": data3
    }

    # Convert JSON object to string
    json_string = json.dumps(combined_data)

    # Return JSON response
    return jsonify(json_string)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
