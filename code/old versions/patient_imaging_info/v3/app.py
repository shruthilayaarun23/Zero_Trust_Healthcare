from flask import Flask, jsonify, request
from pyorthanc import Orthanc

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Connect to Orthanc server
orthanc = Orthanc('http://localhost:8042')

@app.route('/patient_imaging/getModalities', methods=['GET'])
def get_all_modalities():
    modality_list = orthanc.get_modalities()
    return jsonify(modality_list)

@app.route('/patient_imaging/getAllPatients', methods=['GET'])
def get_all_patient_imaging():
    patient_imaging_list = orthanc.get_patients()
    return jsonify(patient_imaging_list)

@app.route('/patient_imaging/getPatientImagingInfo/<string:patient_id>', methods=['GET'])
def get_patient_imaging(patient_id):
    patient = orthanc.get_patient_information(patient_id)
    if patient:
        return jsonify(patient)
    else:
        return jsonify({'error': 'Patient not found'})

@app.route('/patient_imaging', methods=['POST'])
def add_patient_imaging():
    patient_data = request.json
    patient_id = orthanc.create_patient(patient_data)
    return jsonify({'patient_id': patient_id})

@app.route('/patient_imaging/<string:patient_id>', methods=['PUT'])
def update_patient_imaging(patient_id):
    patient_data = request.json
    orthanc.modify_patient(patient_id, patient_data)
    return jsonify({'patient_id': patient_id})

@app.route('/patient_imaging/<string:patient_id>', methods=['DELETE'])
def delete_patient_imaging(patient_id):
    orthanc.delete_patient(patient_id)
    return jsonify({'result': True})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
