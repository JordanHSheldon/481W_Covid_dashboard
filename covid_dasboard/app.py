from flask import Flask, render_template
from datetime import timedelta
from getCovidInfo import getAllStateInfo
from getCovidInfo import getStateInfo
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/testing")
def test():
    return render_template('testing.html', temp = getAllStateInfo())