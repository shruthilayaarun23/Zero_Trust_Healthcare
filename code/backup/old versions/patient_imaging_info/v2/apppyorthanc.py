from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)
app.config['DEBUG'] = True

class OrthancClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path):
        response = requests.get(self.base_url + path)
        response.raise_for_status()
        return response.json()

    def post(self, path, data):
        response = requests.post(self.base_url + path, json=data)
        response.raise_for_status()
        return response.json()

    def put(self, path, data):
        response = requests.put(self.base_url + path, json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, path):
        response = requests.delete(self.base_url + path)
        response.raise_for_status()
        return response.json()

client = OrthancClient('http://localhost:8042')

@app.route('/patient_imaging', methods=['GET'])
def get_all_patients():
    patients = client.get('/patients')
    return jsonify(patients)

@app.route('/patient_imaging/<patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = client.get('/patients/' + patient_id)
    return jsonify(patient)

@app.route('/patient_imaging', methods=['POST'])
def create_patient():
    data = request.json
    patient = client.post('/patients', data)
    return jsonify(patient)

@app.route('/patient_imaging/<patient_id>', methods=['PUT'])
def update_patient(patient_id):
    data = request.json
    patient = client.put('/patients/' + patient_id, data)
    return jsonify(patient)

@app.route('/patient_imaging/<patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    patient = client.delete('/patients/' + patient_id)
    return jsonify(patient)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
