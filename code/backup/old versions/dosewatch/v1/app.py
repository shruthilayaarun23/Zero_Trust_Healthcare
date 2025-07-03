
from flask import Flask, request,render_template
import psycopg2

CREATE_PATIENT = (
    "create table IF not exists medicine_dosage  (m_id SERIAL PRIMARY KEY,p_id integer, name TEXT,doctor_name TEXT,disease TEXT,prescribed_med TEXT,dosage TEXT,duration_med TEXT);"
)

INSERTVAL = (
    "insert into medicine_dosage (p_id,name,doctor_name,disease,prescribed_med,dosage,duration_med) values (%s,%s,%s,%s,%s,%s,%s) returning m_id;"
    )

DISP_PATIENT=(
    "select * from medicine_dosage where p_id=(%s);"


)

app= Flask(__name__)


connection = psycopg2.connect(host='postgresdb', dbname='medicine_dosage', user='postgres', password='scorose23', port=5432)

cursor=connection.cursor()



@app.route("/",methods=['GET','POST'])
def home():
    return render_template('home.html')



@app.route("/create",methods=['POST','GET'])
def create_dosage():
    
    render_template('medhome.html')
    
    p_id=request.form.get('p_id')
    name=request.form.get('name')
    doctor_name=request.form.get('doctor_name')
    disease=request.form.get('disease')
    prescribed_med=request.form.get('prescribed_med')
    dosage=request.form.get('dosage')
    duration_med=request.form.get('duration_med')
    
    cursor.execute(CREATE_PATIENT)

    cursor.execute(INSERTVAL,(p_id,name,doctor_name,disease,prescribed_med,dosage,duration_med))
    m_id = cursor.fetchone()[0]
    connection.commit()
    
    if name != None:
        return render_template('medhome.html',info={"Medicine id ": m_id, "message": f"Patient Record {name} created."})
    else:
        return render_template('medhome.html')

@app.route("/disp",methods=['POST','GET'])
def disp():
    return render_template('disp.html')

@app.route("/read",methods=['POST','GET'])
def read():

    
    p_id=request.form.get('p_id')
    cursor.execute(DISP_PATIENT,(p_id))
    records = cursor.fetchall()

    
    return render_template('disp.html',info=records)

if __name__ =="__main__":
    app.run(port=5001,host="127.0.0.1",debug=True)

    