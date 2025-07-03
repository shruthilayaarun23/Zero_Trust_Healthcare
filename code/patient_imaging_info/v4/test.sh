while sleep 0.1; 
  do 
    curl -X GET  https://127.0.0.1.sslip.io:9443/patient_imaging/getAllPatients --cacert ./istio/ca.crt
    echo ""; 
  done ;