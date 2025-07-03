from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/patient-info/<int:patient_id>')
def get_patient_data(patient_id):
    # Request data from App 1
    dw_response = requests.get(f'https://127.0.0.1.dw.sslip.io:9443/dose-watch')
    dw_data = dw_response.json()

    # Request data from App 2
    pd_response = requests.get(f'https://127.0.0.1.pd.sslip.io:9443/patient-details')
    pd_data = pd_response.json()

    # Request data from App 3
    pi_response = requests.get(f'https://127.0.0.1.pi.sslip.io:9443/patient_imaging')
    pi_data = pi_response.json()

    # Combine the data from all three apps
    patient_data = {
        'patient_id': patient_id,
        'dw_data': dw_data,
        'pd_data': pd_data,
        'pi_data': pi_data
    }

    return jsonify(patient_data)

if __name__ == '__main__':
    app.run(debug=True)
