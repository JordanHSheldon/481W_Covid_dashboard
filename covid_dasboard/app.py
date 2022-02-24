from flask import Flask, render_template, request,redirect
from datetime import timedelta
from getCovidInfo import getAllStateInfo, getCSV, getAllCounties, getAllStates
from getCovidInfo import getStateInfo
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        temp = request.form['search']
        print(temp)
        return redirect("/"+temp)
    else:
        return render_template("home.html")

@app.route("/about", methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        temp = request.form['search']
        return redirect("/"+temp)
    else:
        return render_template("about.html")

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        temp = request.form['search']
        print(temp)
        return redirect("/"+temp)
    else:
        return render_template('dashboard.html', temp = getAllStateInfo())

@app.route("/testing", methods=['GET', 'POST'])
def test():
    getCSV()
    getAllStates()
    return render_template('testing.html', data=getAllCounties())
    

@app.route("/<t>", methods=['GET', 'POST'])
def yes(t):
    if request.method == 'POST':
        temp = request.form['search']
        return redirect("/"+temp)
    else:
        state = '%s' % t 
        return render_template('test.html', temp = getStateInfo(state))