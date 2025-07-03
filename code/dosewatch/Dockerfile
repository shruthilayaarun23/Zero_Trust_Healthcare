FROM registry.fedoraproject.org/fedora-minimal

EXPOSE 5001

RUN microdnf -y install python-pip && microdnf clean all
COPY ./v2 /app

WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]