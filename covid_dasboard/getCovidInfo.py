import urllib.request, json, requests

# old link
link = "https://api.covidactnow.org/v2/counties.csv?apiKey=0600140b5e8f4e179b6c7fdf39dce72f"

# function for specific state info
# if state or territory cant be found, show all states/ territories
def getStateInfo(state):
    if(getState(state)!="null"):
        with urllib.request.urlopen("https://api.covidtracking.com/v1/states/"+str(getState(state))+"/current.json") as url:
            data = json.loads(url.read().decode())
            return(data)
    else:
        with urllib.request.urlopen("https://api.covidtracking.com/v1/states/current.json") as url:
            data = json.loads(url.read().decode())
            return(data)

# function for all state info  
def getAllStateInfo():  
    with urllib.request.urlopen("https://api.covidtracking.com/v1/states/current.json") as url:
        data = json.loads(url.read().decode())
        return(data)

# Method that pulls a csv file from an api
# then saves it locally to be accessed.
def getCSV():
    req = requests.get(link)
    url_content = req.content
    csv_file = open('counties.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()


# Method returns array of dictionaries that contain data on all 
# counties in a given state's covid data
def getState(state):
    results = []
    file_name = "counties.csv"
    file = open(file_name,'r')
    lines = file.readlines()
    for j in range(0,len(lines),1):
        arraysplit = lines[j].split(',')
        d={}
        d['country'] =  arraysplit[1]
        d['state'] =  arraysplit[2]
        d['county'] =  arraysplit[3]
        d['population'] =  arraysplit[8]
        d['testPositiveRatio'] =  arraysplit[9]
        d['metrics.infectionRate'] =  arraysplit[13]
        d['riskLevelsOverall'] =  arraysplit[18]
        d['actualCases'] =  arraysplit[25]
        d['actualDeaths'] =  arraysplit[26]
        d['vacinationsComplete'] = arraysplit[45]
        results.append(d)
    formatted_results=[]
    k = 0
    while(k<len(lines)):
        if(results[k]['state']==str(state).upper()):
            
            formatted_results.append(results[k])
        k+=1
    try:    
        return formatted_results   
    except:
        print()
    


# function that returns a counties data and returns it in the 
# form of an array
def getCounty(state,county):
    temp = getState(state)
    for k in range(0,len(temp),1):
        if(temp[k]['county']==county):
            return temp[k]

# function for getting which state is which rank in most covid cases.
def getStateName(acronym):
    us_state_abbrev = {
            'AL': 'Alabama',
            'AK': 'Alaska',
            'AZ': 'Arizona',
            'AR': 'Arkansas',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'HI': 'Hawaii',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'IA': 'Iowa',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'ME': 'Maine',
            'MD': 'Maryland',
            'MA': 'Massachusetts',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MS': 'Mississippi',
            'MO': 'Missouri',
            'MT': 'Montana',
            'NE': 'Nebraska',
            'NV': 'Nevada',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NY': 'New York',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VT': 'Vermont',
            'VA': 'Virginia',
            'WA': 'Washington',
            'WV': 'West Virginia',
            'WI': 'Wisconsin',
            'WY': 'Wyoming',
            'DC': 'District of Columbia',
            'MP': 'Northern Mariana Islands',
            'PW': 'Palau',
            'PR': 'Puerto Rico',
            'VI': 'Virgin Islands',
            'AA': 'Armed Forces Americas (Except Canada)',
            'AE': 'Armed Forces Africa/Canada/Europe/Middle East',
            'AP': 'Armed Forces Pacific'
        }
    return us_state_abbrev.get(acronym.upper()) 

def processStateName(stateName):
    abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
    }
    state_abbrev = {
    'AL': 'Alabama','AK': 'Alaska','AZ': 'Arizona','AR': 'Arkansas','CA': 'California','CO': 'Colorado','CT': 'Connecticut','DE': 'Delaware',
    'FL': 'Florida','GA': 'Georgia','HI': 'Hawaii','ID': 'Idaho','IL': 'Illinois','IN': 'Indiana','IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky','LA': 'Louisiana','ME': 'Maine','MD': 'Maryland','MA': 'Massachusetts','MI': 'Michigan','MN': 'Minnesota','MS': 
    'Mississippi','MO': 'Missouri','MT': 'Montana','NE': 'Nebraska','NV': 'Nevada','NH': 'New Hampshire','NJ': 'New Jersey','NM': 'New Mexico',
    'NY': 'New York','NC': 'North Carolina','ND': 'North Dakota','OH': 'Ohio','OK': 'Oklahoma','OR': 'Oregon','PA': 'Pennsylvania',
    'RI': 'Rhode Island','SC': 'South Carolina','SD': 'South Dakota','TN': 'Tennessee','TX': 'Texas','UT': 'Utah','VT': 'Vermont',
    'VA': 'Virginia','WA': 'Washington','WV': 'West Virginia','WI': 'Wisconsin','WY': 'Wyoming','DC': 'District of Columbia',
    'MP': 'Northern Mariana Islands','PW': 'Palau','PR': 'Puerto Rico','VI': 'Virgin Islands',
    }
    
    if(len(stateName)>2):
        if stateName in abbrev:
            return abbrev[stateName]
        else:
            return "State not found"
    else:
        if stateName in state_abbrev:
            return stateName
        else:
            return "State not found"

