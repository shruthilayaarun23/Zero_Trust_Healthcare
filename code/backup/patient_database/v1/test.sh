while sleep 0.1; 
  do 
    curl -kv -X POST -F 'p_id=1' https://127.0.0.1.sslip.io:9443/patient-database/read --cacert ./istio/ca.crt
    echo ""; 
  done ;