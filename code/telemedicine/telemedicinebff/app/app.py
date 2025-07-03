from flask import Flask
import requests
import json
import os
from flask import request

version=os.getenv("VERSION")
app = Flask(__name__)

def forwardTraceHeaders(request):
  headers = {}
  incomingheaders = [
    'x-request-id',
    'x-b3-traceid',
    'x-b3-spanid',
    'x-b3-parentspanid',
    'x-b3-sampled',
    'x-b3-flags',
    'x-ot-span-context',
    'x-dev-user'
  ]
 
  for h in incomingheaders:
    val = request.headers.get(h)

    if val is not None:
      headers[h] = val
  
  return headers

@app.route('/combined_data/<int:p_id>/<string:study_id>', methods=['GET'])
def get_combined_data(p_id,study_id):
    headers = forwardTraceHeaders(request)

    pdresponse = requests.get(f"http://patient-details.patient-details:5001/patient-details/getPatientDetails/{p_id}",headers=headers)
    dwresponse = requests.get(f"http://dose-watch.dose-watch:5001/dose-watch/getPatientDosages/{p_id}",headers=headers)
    piresponse = requests.get(f"http://patient-imaging.patient-imaging:5000/patient_imaging/getPatientImagingInfo/{study_id}",headers=headers)

    
    patientdetails = pdresponse.json()
    dosewatch = dwresponse.json()
    patientimaging = piresponse.json()
 
    
    combined_data = {
        "version": version,
        "dosewatch": dosewatch,
        "patientdetails": patientdetails,
        "patientimaging": patientimaging
    }

    
    json_string = json.dumps(combined_data)

    
    data = json.loads(json_string)
    return data


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
