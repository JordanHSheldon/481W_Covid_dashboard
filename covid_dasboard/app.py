from flask import Flask, render_template
from datetime import timedelta
from getCovidInfo import getAllStateInfo
from getCovidInfo import getStateInfo
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

