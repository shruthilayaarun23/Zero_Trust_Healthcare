from flask import Flask, request
from flask_restful import Resource, Api
import requests
import pydicom

app = Flask(__name__)
api = Api(app)

ORTHANC_URL = 'http://localhost:8042'

class PatientImagingInfo(Resource):
    def get(self, patient_id):
        response = requests.get(f'{ORTHANC_URL}/patients/{patient_id}')
        return response.json()

    def post(self):
        dcm_file = request.files['dcm_file']
        dcm_data = pydicom.dcmread(dcm_file)
        headers = {'content-type': 'application/dicom'}
        response = requests.post(f'{ORTHANC_URL}/patients', headers=headers, data=dcm_data.tobytes())
        return response.json()

    def put(self, patient_id):
        dcm_file = request.files['dcm_file']
        dcm_data = pydicom.dcmread(dcm_file)
        headers = {'content-type': 'application/dicom'}
        response = requests.put(f'{ORTHANC_URL}/patients/{patient_id}', headers=headers, data=dcm_data.tobytes())
        return response.json()

    def delete(self, patient_id):
        response = requests.delete(f'{ORTHANC_URL}/patients/{patient_id}')
        return response.json()

api.add_resource(PatientImagingInfo, '/patient_imaging/getAllPatients')
api.add_resource(PatientImagingInfo, '/patient_imaging/getPatientInfo/<string:patient_id>')

if __name__ == '__main__':
    app.run(debug=True)
