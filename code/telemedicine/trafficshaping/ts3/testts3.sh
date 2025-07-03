echo curl  -X GET "http://telemedicinebff.telemedicinebff:5000/combined_data/1/708a2528-b512164c-0f547574-dfbad394-88a66bdc" 
kubectl exec -it $1 -n telemedicinebff -c debug-container -- curl  -X GET "http://telemedicinebff.telemedicinebff:5000/combined_data/1/708a2528-b512164c-0f547574-dfbad394-88a66bdc" 

echo curl  -X GET --header 'version:v2' "http://telemedicinebff.telemedicinebff:5000/combined_data/1/708a2528-b512164c-0f547574-dfbad394-88a66bdc"
kubectl exec -it $1 -n telemedicinebff -c debug-container -- curl  -X GET --header 'version:v2' 'http://telemedicinebff.telemedicinebff:5000/combined_data/1/708a2528-b512164c-0f547574-dfbad394-88a66bdc' 
