from flask import Flask, render_template, request,redirect
from datetime import timedelta
from getCovidInfo import getAllStateInfo, getCSV, getState
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

@app.route("/testing/<t>", methods=['GET', 'POST'])
def test(t):
    getCSV()
    state = '%s' % t 
    return render_template('testing.html', data=getState(state))

@app.route("/<p>", methods=['GET', 'POST'])
def yes(p):
    if request.method == 'POST':
        temp = request.form['search']
        return redirect("/"+temp)
    else:
        state = '%s' % p
        return render_template('test.html', temp = getState(state), state=state)
        