PROJECT=telemedicine
DOCKERREPOSITORY=docker.io/shruthiarun23

DWPROXYNODE=127.0.0.1.dw.sslip.io
PDBPROXYNODE=127.0.0.1.pd.sslip.io
PIPROXYNODE=127.0.0.1.pi.sslip.io
TMPROXYNODE=127.0.0.1.tm.sslip.io


DOSE-WATCH=$(DOCKERREPOSITORY)/dosewatch
PATIENT-DATABASE=$(DOCKERREPOSITORY)/patient-database
FORTIO_POD=$(shell kubectl get pod  -l app=fortio -o jsonpath='{.items[0].metadata.name}')
DEBUG_POD=$(shell kubectl get pod -n telemedicinebff -l app=curl -o jsonpath='{.items[0].metadata.name}')

init:
	-bash -c 'kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.10.1/cert-manager.yaml'
	-bash -c 'kubectl apply -f ./ingresscerts/rootca.yaml'
	
clean:
	-bash -c 'kubectl delete -f ./ingresscerts/rootca.yaml'
	-bash -c 'kubectl delete -f https://github.com/cert-manager/cert-manager/releases/download/v1.10.1/cert-manager.yaml'

init-dw:
	-bash -c 'kubectl create ns dose-watch'
	-bash -c 'kubectl label ns dose-watch istio-injection=enabled'

	-bash -c 'kubectl apply -f ./dosewatch/istio/destinationrules.yaml'	
	-bash -c 'kubectl apply -f ./dosewatch/istio/virtualservice.yaml'	

	-bash -c 'kubectl apply -f ./dosewatch/istio/gateway.yaml'	
	-bash -c 'kubectl apply -f ./dosewatch/istio/mtls.yaml'	
    
	-bash -c 'kubectl apply -f ./dosewatch/istio/dosewatch-certs.yaml'	
	-bash -c 'kubectl apply -f ./dosewatch/app/app-service.yaml'	

	-bash -c 'kubectl apply -f  ./dosewatch/database/db-configmap.yaml'
	-bash -c 'kubectl apply -f ./dosewatch/database/db-volume-claim.yaml'
	-bash -c 'kubectl apply -f ./dosewatch/database/db-service.yaml'
	
deploy-dw:
	-bash -c 'kubectl apply -f ./dosewatch/app/app-deployment.yaml'
	-bash -c 'kubectl apply -f ./dosewatch/database/db-deployment.yaml'

clean-dw:
	-bash -c 'kubectl delete -f ./dosewatch/istio/destinationrules.yaml'	
	-bash -c 'kubectl delete -f ./dosewatch/istio/virtualservice.yaml'	

	-bash -c 'kubectl delete -f ./dosewatch/istio/gateway.yaml'	
	-bash -c 'kubectl delete -f ./dosewatch/istio/mtls.yaml'	
		
    	
	
	-bash -c 'kubectl delete -f ./dosewatch/istio/dosewatch-certs.yaml'	
	-bash -c 'kubectl delete -f ./dosewatch/app/app-service.yaml'

	-bash -c 'kubectl delete -f  ./dosewatch/database/db-configmap.yaml'
	-bash -c 'kubectl delete -f ./dosewatch/database/db-volume-claim.yaml'
	-bash -c 'kubectl delete -f ./dosewatch/database/db-service.yaml'
	-bash -c 'kubectl delete -f  ./dosewatch/database/db-deployment.yaml'
    

	-bash -c 'kubectl delete ns dose-watch'	

test-dw:
	-bash -c './dosewatch/app/test.sh $(DWPROXYNODE)'	

init-pd:
	-bash -c 'kubectl create ns patient-details'
	-bash -c 'kubectl label ns patient-details istio-injection=enabled'

	-bash -c 'kubectl apply -f ./patient-details/istio/destinationrules.yaml'	
	-bash -c 'kubectl apply -f ./patient-details/istio/virtualservice.yaml'	

	-bash -c 'kubectl apply -f ./patient-details/istio/gateway.yaml'	
	-bash -c 'kubectl apply -f ./patient-details/istio/mtls.yaml'	
    
	-bash -c 'kubectl apply -f ./patient-details/istio/patientdatabase-certs.yaml'	
	-bash -c 'kubectl apply -f ./patient-details/app/app-service.yaml'	

	-bash -c 'kubectl apply -f  ./patient-details/database/db-configmap.yaml'
	-bash -c 'kubectl apply -f ./patient-details/database/db-volume-claim.yaml'
	-bash -c 'kubectl apply -f ./patient-details/database/db-service.yaml'
	

deploy-pd:
	-bash -c 'kubectl apply -f ./patient-details/app/app-deployment.yaml'
	-bash -c 'kubectl apply -f ./patient-details/database/db-deployment.yaml'

clean-pd:
	-bash -c 'kubectl delete -f ./patient-details/istio/destinationrules.yaml'	
	-bash -c 'kubectl delete -f ./patient-details/istio/virtualservice.yaml'	

	-bash -c 'kubectl delete -f ./patient-details/istio/gateway.yaml'	
	-bash -c 'kubectl delete -f ./patient-details/istio/mtls.yaml'	
	
	-bash -c 'kubectl delete -f ./patient-details/istio/patientdatabase-certs.yaml'	
	-bash -c 'kubectl delete -f ./patient-details/app/app-service.yaml'

	-bash -c 'kubectl delete -f  ./patient-details/database/db-configmap.yaml'
	-bash -c 'kubectl delete -f ./patient-details/database/db-volume-claim.yaml'
	-bash -c 'kubectl delete -f ./patient-details/database/db-service.yaml'
	-bash -c 'kubectl delete -f  ./patient-details/database/db-deployment.yaml'

	-bash -c 'kubectl delete ns patient-details'

test-pdb:
	-bash -c './patient-details/app/test.sh $(PDBPROXYNODE)'

init-pi:
	-bash -c 'kubectl create ns patient-imaging'
	-bash -c 'kubectl label ns patient-imaging istio-injection=enabled'

	-bash -c 'kubectl apply -f ./patient-imaging/istio/destinationrules.yaml'	
	-bash -c 'kubectl apply -f ./patient-imaging/istio/virtualservice.yaml'	

	-bash -c 'kubectl apply -f ./patient-imaging/istio/gateway.yaml'	
	-bash -c 'kubectl apply -f ./patient-imaging/istio/mtls.yaml'	
    
	-bash -c 'kubectl apply -f ./patient-imaging/istio/patientimaging-certs.yaml'	
	-bash -c 'kubectl apply -f ./patient-imaging/app/app-service.yaml'	

	-bash -c 'kubectl apply -f  ./patient-imaging/orthanc/orthanc_deploy.yaml'
	-bash -c 'kubectl apply -f  ./patient-imaging/orthanc/orthanc_pvc.yaml'
	-bash -c 'kubectl apply -f ./patient-imaging/orthanc/orthanc_svc.yaml'
	
deploy-pi:
	-bash -c 'kubectl apply -f ./patient-imaging/app/app-deployment.yaml'


clean-pi:
	-bash -c 'kubectl delete -f ./patient-imaging/istio/destinationrules.yaml'	
	-bash -c 'kubectl delete -f ./patient-imaging/istio/virtualservice.yaml'	

	-bash -c 'kubectl delete -f ./patient-imaging/istio/gateway.yaml'	
	-bash -c 'kubectl delete -f ./patient-imaging/istio/mtls.yaml'	
    
	-bash -c 'kubectl delete -f ./patient-imaging/istio/patientimaging-certs.yaml'	
	-bash -c 'kubectl delete -f ./patient-imaging/app/app-service.yaml'	

	-bash -c 'kubectl delete -f  ./patient-imaging/orthanc/orthanc_deploy.yaml'
	-bash -c 'kubectl delete -f  ./patient-imaging/orthanc/orthanc_pvc.yaml'
	-bash -c 'kubectl delete -f ./patient-imaging/orthanc/orthanc_svc.yaml'
	
	-bash -c 'kubectl delete ns patient-imaging'
test-pi:
	-bash -c './patient-imaging/app/test.sh $(PIPROXYNODE)'

init-tmbff:
	-bash -c 'kubectl create ns telemedicinebff'
	-bash -c 'kubectl label ns telemedicinebff istio-injection=enabled'

	-bash -c 'kubectl apply -f ./telemedicinebff/istio/destinationrules.yaml'
	-bash -c 'kubectl apply -f ./telemedicinebff/istio/virtualservice.yaml'	

	-bash -c 'kubectl apply -f ./telemedicinebff/istio/gateway.yaml'	
	-bash -c 'kubectl apply -f ./telemedicinebff/istio/mtls.yaml'	

    
	-bash -c 'kubectl apply -f ./telemedicinebff/istio/telemedicine-certs.yaml'	
	-bash -c 'kubectl apply -f ./telemedicinebff/app/app-service.yaml'
	
deploy-tmbff:
	-bash -c 'kubectl apply -f ./telemedicinebff/app/app-deployment.yaml'

clean-tmbff:
	-bash -c 'kubectl delete -f ./telemedicinebff/istio/destinationrules.yaml'			
	-bash -c 'kubectl delete -f ./telemedicinebff/istio/mtls.yaml'
	
	-bash -c 'kubectl delete -f ./telemedicinebff/istio/gateway.yaml'	
	-bash -c 'kubectl delete -f ./telemedicinebff/istio/virtualservice.yaml'		
     
	-bash -c 'kubectl delete -f ./telemedicinebff/istio/telemedicine-certs.yaml'	
	-bash -c 'kubectl delete -f ./telemedicinebff/app/app-deployment.yaml'
	-bash -c 'kubectl delete -f ./telemedicinebff/app/app-service.yaml'

	-bash -c 'kubectl delete ns telemedicinebff'

test-tmbff:
	-bash -c './telemedicinebff/app/testbff.sh $(TMPROXYNODE)'

init-tmapp:
	-bash -c 'kubectl create ns telemedicineapp'
	-bash -c 'kubectl label ns telemedicineapp istio-injection=enabled'
    
	-bash -c 'kubectl apply -f ./telemedicineapp/istio/destinationrules.yaml'
	-bash -c 'kubectl apply -f ./telemedicineapp/istio/mtls.yaml'	

deploy-tmapp:	
	-bash -c 'kubectl apply -f ./telemedicineapp/app/app-deployment.yaml'

clean-tmapp:
	-bash -c 'kubectl delete -f ./telemedicineapp/istio/destinationrules.yaml'			
	-bash -c 'kubectl delete -f ./telemedicineapp/istio/mtls.yaml'
	
	-bash -c 'kubectl delete -f ./telemedicineapp/app/app-deployment.yaml'
	-bash -c 'kubectl delete ns telemedicineapp'

test-tmapp:
	-bash -c './telemedicineapp/app/test.sh $(TMPROXYNODE)'

init-ts1:
	-bash -c 'kubectl apply -f ./trafficshaping/ts1/trafficshifting-1.yaml'

clean-ts1:
	-bash -c 'kubectl delete -f ./trafficshaping/ts1/trafficshifting-1.yaml'

init-ts2:
	-bash -c 'kubectl apply -f ./trafficshaping/ts2/trafficshifting-2.yaml'

clean-ts2:
	-bash -c 'kubectl delete -f ./trafficshaping/ts2/trafficshifting-2.yaml'

init-ts3:
	-bash -c 'kubectl apply -f ./trafficshaping/ts3/trafficshifting-3.yaml'

clean-ts3:
	-bash -c 'kubectl delete -f ./trafficshaping/ts3/trafficshifting-3.yaml'

test-ts3:
	-bash -c './trafficshaping/ts3/testts3.sh $(DEBUG_POD) $(TMPROXYNODE)'

init-mirror:
	-bash -c 'kubectl apply -f ./mirror/trafficmirroring.yaml'

clean-mirror:
	-bash -c 'kubectl delete -f ./mirror/trafficmirroring.yaml'

test-mirror:
	-bash -c './mirror/testmirroring.sh $(TMPROXYNODE)'

init-sp1:
	-bash -c 'kubectl apply -f ./securitypolicy/securitypolicy.yaml'

clean-sp1:
	-bash -c 'kubectl delete -f ./securitypolicy/securitypolicy.yaml'

init-sp2:
	-bash -c 'kubectl apply -f ./securitypolicy/sp-2.yaml'

clean-sp2:
	-bash -c 'kubectl delete -f ./securitypolicy/sp-2.yaml'

init-rl:
	-bash -c 'kubectl apply -f ./ratelimit/ratelimit.yaml'

clean-rl:
	-bash -c 'kubectl delete -f ./ratelimit/ratelimit.yaml'

init-fd:
	-bash -c 'kubectl apply -f ./fixedelay/fixedelay.yaml'

clean-fd:
	-bash -c 'kubectl delete -f ./fixedelay/fixedelay.yaml'

init-fi:
	-bash -c 'kubectl apply -f ./faultinjection/faultinjection.yaml'

clean-fi:
	-bash -c 'kubectl delete -f ./faultinjection/faultinjection.yaml'

init-cb:
	-bash -c 'kubectl apply -f ./circuitbreaker/circuitbreaker.yaml'

clean-cb:
	-bash -c 'kubectl delete -f ./circuitbreaker/circuitbreaker.yaml'

test-cb:
	-bash -c 'kubectl exec -it $(FORTIO_POD)  -c fortio fortio -- load -curl "http://telemedicinebff.telemedicinebff:5000/combined_data/1/708a2528-b512164c-0f547574-dfbad394-88a66bdc"'


restart-all:
	kubectl delete pods --all -n $(PROJECT)
