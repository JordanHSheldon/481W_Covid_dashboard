from tokenize import Double
from flask import Flask, render_template, request,redirect
from datetime import timedelta
from getCovidInfo import getAllStateInfo, getCSV, getState,getStateName
app = Flask(__name__)

abbrev = {
    "alabama": "AL","alaska": "AK","arizona": "AZ","arkansas": "AR","california": "CA","colorado": "CO","connecticut": "CT","delaware": "DE",
    "florida": "FL","georgia": "GA","hawaii": "HI","idaho": "ID","illinois": "IL","indiana": "IN","iowa": "IA","kansas": "KS",
    "kentucky": "KY","louisiana": "LA","maine": "ME","maryland": "MD","massachusetts": "MA","michigan": "MI","minnesota": "MN","mississippi": "MS","missouri": "MO",
    "montana": "MT","Nebraska": "NE","Nevada": "NV","New Hampshire": "NH","New Jersey": "NJ","newmexico": "NM","New York": "NY","north Carolina": "NC",
    "north dakota": "ND","ohio": "OH","oklahoma": "OK","oregon": "OR","pennsylvania": "PA","rhode Island": "RI","southcarolina": "SC","south Dakota": "SD",
    "Tennessee": "TN","Texas": "TX","Utah": "UT","Vermont": "VT","Virginia": "VA","Washington": "WA","West Virginia": "WV","wisconsin": "WI",
    "wyoming": "WY","district of columbia": "DC","americansamoa": "AS","guam": "GU","northern mariana islands": "MP","puerto rico": "PR",
    "unitedstatesminoroutlyingislands": "UM",
    "U.S. virginislands": "VI",
    }
state_abbrev = {
    'AL': 'alabama','AK': 'alaska','AZ': 'arizona','AR': 'arkansas','CA': 'california','CO': 'colorado','CT': 'connecticut','DE': 'delaware',
    'FL': 'florida','GA': 'georgia','HI': 'hawaii','ID': 'idaho','IL': 'illinois','IN': 'indiana','IA': 'iowa',
    'KS': 'kansas', 'KY': 'kentucky','LA': 'louisiana','ME': 'maine','MD': 'maryland','MA': 'massachusetts','MI': 'michigan','MN': 'minnesota','MS': 
    'mississippi','MO': 'missouri','MT': 'montana','NE': 'Nebraska','NV': 'Nevada','NH': 'newhampshire','NJ': 'newjersey','NM': 'newmexico',
    'NY': 'new York','NC': 'northcarolina','ND': 'northdakota','OH': 'ohio','OK': 'oklahoma','OR': 'oregon','PA': 'pennsylvania',
    'RI': 'rhode Island','SC': 'southcarolina','SD': 'southdakota','TN': 'Tennessee','TX': 'texas','UT': 'utah','VT': 'vermont',
    'VA': 'virginia','WA': 'washington','WV': 'westvirginia','WI': 'wisconsin','WY': 'wyoming','DC': 'districtofcolumbia',
    'MP': 'northernmarianaislands','PW': 'palau','PR': 'puertorico','VI': 'virgin Islands',
    }




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
        #checking to see if the state exists in our system
        if(len(state)>2):
            if state in abbrev:
                state = abbrev[state.lower()]
            else:
                state = "NA"
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
            if(float(x[k]["vacinationsComplete"]!="")):
                tempVac = float(x[k]["vacinationsComplete"])
            else:
                tempVac = 0
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
        # return the html file and passing in the correct information.
        return render_template('test.html', temp = x, state=getStateName(state), ack = state, total = d)
        
