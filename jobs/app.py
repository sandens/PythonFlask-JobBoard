from flask import Flask, render_template, g
import sqlite3

PATH="db/jobs.sqlite"

app = Flask(__name__)

def open_connection():
   connection= getattr(g,'_connection',None)
   if connection is None:
       connection =g._connection = sqlite3.connect(PATH)
   connection.row_factory = sqlite3.Row
   return connection    

@app.teardown_appcontext   
def close_connection(exception):
    connection= getattr(g,'_connection',None)
    if connection is not None:
       connection.close()


def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection()
    cursor = connection.execute(sql,values)

    if commit is True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()
    cursor.close()

    return results

@app.route("/")
@app.route("/jobs")
def jobs():
    ''' added jobs route'''
    jobs = execute_sql(
        "SELECT job.id ,job.title,job.salary,job.description, \
         employee.id  as employer_id, employer.name as employer_name from job \
           JOIN employer ON employer.id = job.employer.id")

    return render_template("index.html", jobs=jobs)