from tokenize import Double
from flask import Flask, render_template, request,redirect
from datetime import timedelta
from getCovidInfo import getAllStateInfo, getCSV, getState,getStateName
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
        x = getState(state)
        d = []
        h = 0
        totalPopulation=0
        totalCases=0
        totalDeaths=0
        totalVaccination = 0

        for k in range(0,len(x),1):
            tempPop = int(x[k]["population"])
            tempCases = int(x[k]["actualCases"])
            tempDeaths = int(x[k]["actualDeaths"])
            tempVac = float(x[k]["vacinationsComplete"])
            totalPopulation+=tempPop
            totalCases+=tempCases
            totalDeaths+=tempDeaths
            totalVaccination+=tempVac
            h+=1
        d.append(totalPopulation)
        d.append(totalCases)
        d.append(totalDeaths)
        
        try:
            why = totalVaccination/(len(x))*100
            d.append("%.1f" % why)
        except:
            print()
        return render_template('test.html', temp = x, state=getStateName(state), ack = state, total = d)
        