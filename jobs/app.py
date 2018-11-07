from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/jobs")
def jobs():
    ''' added jobs route'''
    return render_template("index.html")
    

