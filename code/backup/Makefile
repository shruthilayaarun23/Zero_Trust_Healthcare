PROJECT=telemedicine
DOCKERREPOSITORY=docker.io/shruthiarun23

PROXYNODE=localhost:9080

PROXY=$(PROXYNODE)

DOSE-WATCH=$(DOCKERREPOSITORY)/dosewatch
PATIENT-DATABASE=$(DOCKERREPOSITORY)/patient-database

init:
	-bash -c 'kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.10.1/cert-manager.yaml'
	
	-bash -c 'kubectl create ns $(PROJECT)'
	-bash -c 'kubectl label ns $(PROJECT) istio-injection=enabled'

	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./istio/destinationrules.yaml  | kubectl apply -f -	
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./istio/virtualservice.yaml  | kubectl apply -f -		

	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./istio/gateway.yaml  | kubectl apply -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./istio/mtls.yaml | kubectl apply -f -

	-bash -c 'kubectl apply -f ./istio/rootca.yaml'
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./istio/ingress-certs.yaml | kubectl apply -f -

clean:
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./istio/gateway.yaml  | kubectl delete -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./istio/destinationrules.yaml  | kubectl delete -f -	
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./istio/virtualservice.yaml  | kubectl delete -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./istio/mtls.yaml  | kubectl delete -f -

	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./istio/rootca.yaml  | kubectl delete -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./istio/ingress-certs.yaml  | kubectl delete -f -

	-bash -c 'kubectl delete ns $(PROJECT)'	
	-bash -c 'kubectl delete -f https://github.com/cert-manager/cert-manager/releases/download/v1.10.1/cert-manager.yaml'

init-dw:
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./dosewatch/v2/app-service.yaml  | kubectl apply -f -

deploy-dw:
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./dosewatch/v2/app-deployment.yaml  | kubectl apply -f -

clean-dw:
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./dosewatch/v2/app-service.yaml | kubectl delete -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./dosewatch/v2/app-deployment.yaml | kubectl delete -f -

test-dw:
	-bash -c './dosewatch/v2/test.sh $(PROXY)'	

init-pdb:
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./patient_database/v1/app-service.yaml | kubectl apply -f -

deploy-pdb:
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./patient_database/v1/app-deployment.yaml | kubectl apply -f -

clean-pdb:
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./patient_database/v1/app-service.yaml | kubectl delete -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./patient_database/v1/app-deployment.yaml | kubectl delete -f -
test-pdb:
	-bash -c './patient_database/v1/test.sh $(PROXY)'	

init-pg:
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./database/db-configmap.yaml | kubectl apply -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./database/db-persistent-volume.yaml | kubectl apply -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./database/db-volume-claim.yaml | kubectl apply -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./database/db-service.yaml | kubectl apply -f -

deploy-pg:
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./database/db-deployment.yaml | kubectl apply -f -
	
clean-pg:
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./database/db-configmap.yaml | kubectl delete -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./database/db-volume-claim.yaml | kubectl delete -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./database/db-persistent-volume.yaml | kubectl delete -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./database/db-deployment.yaml | kubectl delete -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./database/db-service.yaml | kubectl delete -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./database/db-service.yaml | kubectl delete -f -

init-pi:
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./patient_imaging_info/v4/app-service.yaml | kubectl apply -f -

deploy-pi:
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./patient_imaging_info/v4/app-deployment.yaml | kubectl apply -f -

clean-pi:
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./patient_imaging_info/v4/app-service.yaml | kubectl delete -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./patient_imaging_info/v4/app-deployment.yaml | kubectl delete -f -

test-pi:
	-bash -c './patient_imaging_info/v4/test.sh $(PROXY)'	

init-orthanc:
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./orthanc/orthanc_pvc.yaml | kubectl apply -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./orthanc/orthanc_svc.yaml | kubectl apply -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./orthanc/orthanc_deploy.yaml | kubectl apply -f -


clean-orthanc:
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./orthanc/orthanc-pvc.yaml | kubectl delete -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./orthanc/orthanc-svc.yaml | kubectl delete -f -
	-sed -e 's~<PROJECT>~$(PROJECT)~g' ./orthanc/orthanc-deploy.yaml | kubectl delete -f -
	

restart-all:
	kubectl delete pods --all -n $(PROJECT)
