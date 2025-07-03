
from flask import Flask, request,render_template
import psycopg2
import os
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

CREATE_PATIENT = (
    "create table IF not exists patient_details  (p_id SERIAL PRIMARY KEY, name TEXT,age INT,sex TEXT,contact TEXT,address TEXT,I_id TEXT);"
)

INSERTVAL = (
    "insert into patient_details (name,age,sex,contact,address,I_id) values (%s,%s,%s,%s,%s,%s) returning p_id;"
    )

DISP_PATIENT=(
    "select * from patient_details where p_id=(%s);"


)

app= Flask(__name__)


#connection = psycopg2.connect(host='postgresdb', dbname='patient_details', user='postgres', password='scorose23', port=5432)
#cursor=connection.cursor()
def create_connection():
    #connection = psycopg2.connect(host='postgresdb', dbname='patient_details', user='postgres', password='scorose23', port=5432)
    connection = psycopg2.connect(
    host=POSTGRES_HOST,
    dbname=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    port=POSTGRES_PORT
)
    cursor = connection.cursor()

    return connection, cursor

def close_connection(connection, cursor):
    cursor.close()
    connection.close()


@app.route("/patient-details",methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route("/patient-details/make",methods=['POST','GET'])
def make():
    return render_template('medhome.html')


@app.route("/patient-details/create",methods=['POST','GET'])
def create():
    
    if request.method=='POST':
        connection, cursor = create_connection()
        name=request.form.get('Name')
        age=request.form.get('age')
        sex=request.form.get('sex')
        contact=request.form.get('contact')
        address=request.form.get('address')
        I_id=request.form.get('I_id')
        
        cursor.execute(CREATE_PATIENT)

        cursor.execute(INSERTVAL,(name,age,sex,contact,address,I_id))
        p_id = cursor.fetchone()[0]
        connection.commit()
        close_connection(connection, cursor)
    if name != None:

        return render_template('medhome.html',info=f"{p_id}:{name}'s record was created successfully ")
    # else:
    #     return render_template('medhome.html')

@app.route("/patient-details/disp",methods=['POST','GET'])
def disp():
    return render_template('disp.html')

@app.route("/patient-details/read",methods=['POST','GET'])
def read():

    connection,cursor=create_connection()

    p_id=request.form.get('p_id')
    cursor.execute(DISP_PATIENT,(p_id))
    records = cursor.fetchall()
    close_connection(connection,cursor)
    
    return render_template('disp.html',info=f"Patient id: {records[0][0]}, Name: {records[0][1]}, Age: {records[0][2]}, Sex: {records[0][3]}, Contact: {records[0][4]}, Address: {records[0][5]}, Inurance Id: {records[0][6]} ")

if __name__ =="__main__":
    app.run(port=5001,host="0.0.0.0",debug=True)

    