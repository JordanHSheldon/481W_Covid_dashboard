from tokenize import Double
from flask import Flask, render_template, request,redirect
from datetime import timedelta
from getCovidInfo import getAllStateInfo, getCSV, getState,getStateName
app = Flask(__name__)

abbrev = {
    "alabama": "AL","alaska": "AK","arizona": "AZ","arkansas": "AR","california": "CA","colorado": "CO","connecticut": "CT","delaware": "DE",
    "florida": "FL","georgia": "GA","hawaii": "HI","idaho": "ID","illinois": "IL","indiana": "IN","iowa": "IA","kansas": "KS",
    "kentucky": "KY","louisiana": "LA","maine": "ME","maryland": "MD","massachusetts": "MA","michigan": "MI","minnesota": "MN","mississippi": "MS","missouri": "MO",
    "montana": "MT","Nebraska": "NE","Nevada": "NV","New Hampshire": "NH","New Jersey": "NJ","New Mexico": "NM","New York": "NY","North Carolina": "NC",
    "north dakota": "ND","ohio": "OH","oklahoma": "OK","oregon": "OR","pennsylvania": "PA","rhode Island": "RI","south Carolina": "SC","south Dakota": "SD",
    "Tennessee": "TN","Texas": "TX","Utah": "UT","Vermont": "VT","Virginia": "VA","Washington": "WA","West Virginia": "WV","Wisconsin": "WI",
    "wyoming": "WY","district of columbia": "DC","american Samoa": "AS","Guam": "GU","northern mariana islands": "MP","puerto rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
    }
state_abbrev = {
    'AL': 'alabama','AK': 'alaska','AZ': 'arizona','AR': 'arkansas','CA': 'california','CO': 'colorado','CT': 'connecticut','DE': 'delaware',
    'FL': 'florida','GA': 'georgia','HI': 'hawaii','ID': 'idaho','IL': 'illinois','IN': 'indiana','IA': 'iowa',
    'KS': 'kansas', 'KY': 'kentucky','LA': 'louisiana','ME': 'maine','MD': 'maryland','MA': 'massachusetts','MI': 'michigan','MN': 'Minnesota','MS': 
    'mississippi','MO': 'Missouri','MT': 'Montana','NE': 'Nebraska','NV': 'Nevada','NH': 'New Hampshire','NJ': 'New Jersey','NM': 'New Mexico',
    'NY': 'new York','NC': 'North Carolina','ND': 'North Dakota','OH': 'Ohio','OK': 'Oklahoma','OR': 'Oregon','PA': 'Pennsylvania',
    'RI': 'rhode Island','SC': 'South Carolina','SD': 'South Dakota','TN': 'Tennessee','TX': 'Texas','UT': 'Utah','VT': 'Vermont',
    'VA': 'virginia','WA': 'Washington','WV': 'West Virginia','WI': 'Wisconsin','WY': 'Wyoming','DC': 'District of Columbia',
    'MP': 'northern mariana islands','PW': 'Palau','PR': 'Puerto Rico','VI': 'Virgin Islands',
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
        
