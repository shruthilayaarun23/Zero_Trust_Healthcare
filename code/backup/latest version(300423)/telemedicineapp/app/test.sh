while sleep 0.1;
  do
    curl -F  http://patient-details.patient-details:5001/patient-details/getPatientDetails/1
    curl -F  http://dose-watch.dose-watch:5001/dose-watch/getPatientDosages/1
    curl -F http://patient-imaging.patient-imaging:5000/patient_imaging/getPatientImagingInfo/708a2528-b512164c-0f547574-dfbad394-88a66bdc
    echo "";
  done ;