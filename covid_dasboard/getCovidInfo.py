import urllib.request, json 
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


# function that returns a state or territories
# two letter acronym
def getState(temp):
    us_state_to_abbrev = {
    "alabama": "AL","alaska": "AK","arizona": "AZ","arkansas": "AR",
    "california": "CA","colorado": "CO","connecticut": "CT",
    "delaware": "DE","florida": "FL","georgia": "GA","hawaii": "HI",
    "idaho": "ID","illinois": "IL","indiana": "IN","iowa": "IA",
    "kansas": "KS","kentucky": "KY","louisiana": "LA","maine": "ME",
    "maryland": "MD","massachusetts": "MA","michigan": "MI","minnesota": "MN",
    "mississippi": "MS","missouri": "MO","montana": "MT","nebraska": "NE",
    "nevada": "NV","new Hampshire": "NH","new Jersey": "NJ","new Mexico": "NM",
    "new York": "NY","north Carolina": "NC","north Dakota": "ND","ohio": "OH",
    "oklahoma": "OK","oregon": "OR","pennsylvania": "PA","rhode Island": "RI",
    "south Carolina": "SC","south Dakota": "SD","tennessee": "TN","texas": "TX",
    "utah": "UT","vermont": "VT","virginia": "VA","washington": "WA",
    "west Virginia": "WV","wisconsin": "WI","wyoming": "WY","district of columbia": "DC",
    "american samoa": "AS","guam": "GU","northern mariana islands": "MP",
    "puerto rico": "PR","united states minor outlying islands": "UM",
    "u.s. virgin islands": "VI",
}
    temp = temp.lower()
    if(len(temp)==2):
        return temp
    elif(len(temp)>2):
        if(temp in us_state_to_abbrev.keys()):
            return us_state_to_abbrev[temp].lower()
        else:
            return "null"
    else:
        return "null"


# function for getting which state is which rank in most covid cases.
def getCovidRank():
    return None