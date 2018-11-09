from flask import Fl ask, render_template, g
import sqlite3

DBPATH="db/jobs.sqlite"

app = Flask(__name__)


def open_connection():
   connection= getattr(g,'_connection',None)
   if connection is None:
       connection =g._connection = sqlite3.connect(DBPATH)
   connection.row_factory = sqlite3.Row
   return connection    


@app.teardown_appcontext   
def close_connectin(exception):
     connection =g._connection = sqlite3.connect(DBPATH)
     if connection is not None:
         connection.close()




def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection()
    cursor = connection.execute_sql(sql,values)

    if commit == True:
        results = connection.commit()
    else:
        results = cursor.fetchOne is single else cursor.fetchall()
    return results


@app.route("/")
@app.route("/jobs")
def jobs():
    ''' added jobs route'''
    return render_template("index.html")
    

