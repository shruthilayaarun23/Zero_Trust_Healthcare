
from flask import Flask, request,render_template
import psycopg2
import os

CREATE_PATIENT = ("create table IF not exists medicine_dosage  (m_id SERIAL PRIMARY KEY,p_id integer, name TEXT,doctor_name TEXT,disease TEXT,prescribed_med TEXT,dosage TEXT,duration_med TEXT);")

INSERTVAL = ("insert into medicine_dosage (p_id,name,doctor_name,disease,prescribed_med,dosage,duration_med) values (%s,%s,%s,%s,%s,%s,%s) returning m_id;")

DISP_PATIENT=("select * from medicine_dosage where p_id=(%s);")

app= Flask(__name__)

#connection = psycopg2.connect(host='postgresdb', dbname='medicine_dosage', user='postgres', password='scorose23', port=5432)
#cursor=connection.cursor()

def create_connection():
    connection = psycopg2.connect(host='postgresdb', dbname='medicine_dosage', user='postgres', password='scorose23', port=5432)
    cursor = connection.cursor()

    return connection, cursor

def close_connection(connection, cursor):
    cursor.close()
    connection.close()

@app.route("/dose-watch",methods=['GET','POST'])
def home():
    print(os.getcwd())
    return render_template("home.html")
    

@app.route("/dose-watch/make",methods=['POST','GET'])
def make():
    return render_template("medhome.html")

@app.route("/dose-watch/create",methods=['POST','GET'])
def create_dosage():
    # render_template('medhome.html')
    if request.method=='POST':
        connection, cursor = create_connection()

        p_id=request.form.get('p_id')
        name=request.form.get('Name')
        doctor_name=request.form.get('doctor_name')
        disease=request.form.get('disease')
        prescribed_med=request.form.get('prescribed_med')
        dosage=request.form.get('dosage')
        duration_med=request.form.get('duration_med')
        
        cursor.execute(CREATE_PATIENT)

        cursor.execute(INSERTVAL,(p_id,name,doctor_name,disease,prescribed_med,dosage,duration_med))
        m_id = cursor.fetchone()[0]

        connection.commit()
        close_connection(connection, cursor)    
    if name != None:
        return render_template("medhome.html",info={"Medicine id ": m_id, "message": f"Patient Record {name} created."})
    else:
        return render_template("medhome.html")

@app.route("/dose-watch/disp",methods=['POST','GET'])
def disp():
    return render_template("disp.html")

@app.route("/dose-watch/read",methods=['POST','GET'])
def read():
    connection,cursor=create_connection()

    p_id=request.form.get('p_id')
    cursor.execute(DISP_PATIENT,(p_id))
    records = cursor.fetchall()

    close_connection(connection,cursor)
    return render_template("disp.html",info=records)

if __name__ =="__main__":
    app.run(port=5001,host="0.0.0.0",debug=True)

    