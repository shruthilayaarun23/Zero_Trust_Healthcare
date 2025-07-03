PROJECT=telemedicine
DOCKERREPOSITORY=docker.io/shruthiarun23

DWPROXYNODE=127.0.0.1.dw.sslip.io
PDBPROXYNODE=127.0.0.1.pd.sslip.io
PIPORXYNODE=127.0.0.1.pi.sslip.io



DOSE-WATCH=$(DOCKERREPOSITORY)/dosewatch
PATIENT-DATABASE=$(DOCKERREPOSITORY)/patient-database

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
	-bash -c 'kubectl apply -f  ./dosewatch/database/db-persistent-volume.yaml'
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
	-bash -c 'kubectl delete -f  ./dosewatch/database/db-persistent-volume.yaml'
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
	-bash -c 'kubectl apply -f  ./patient-details/database/db-persistent-volume.yaml'
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
	-bash -c 'kubectl delete -f  ./patient-details/database/db-persistent-volume.yaml'
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

init-tm:
	-bash -c 'kubectl create ns telemedicine'
	-bash -c 'kubectl label ns telemedicine istio-injection=enabled'

	-bash -c 'kubectl apply -f ./telemedicineapp/istio/destinationrules.yaml'		
	-bash -c 'kubectl apply -f ./telemedicineapp/istio/mtls.yaml'	
	
deploy-tm:
	-bash -c 'kubectl apply -f ./telemedicineapp/app/app-deployment.yaml'

clean-tm:
	-bash -c 'kubectl delete -f ./telemedicineapp/istio/destinationrules.yaml'			
	-bash -c 'kubectl delete -f ./telemedicineapp/istio/mtls.yaml'
    
	
	-bash -c 'kubectl delete -f ./telemedicineapp/app/app-deployment.yaml'
	-bash -c 'kubectl delete ns telemedicine'

test-tm:
	-bash -c './telemedicineapp/app/test.sh $(PIPROXYNODE)'

restart-all:
	kubectl delete pods --all -n $(PROJECT)
