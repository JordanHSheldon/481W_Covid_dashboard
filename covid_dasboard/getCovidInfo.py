import urllib.request, json, requests
from contextlib import closing
stateList = ['AK','AL', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FM', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MH', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY' ];


link = "https://api.covidactnow.org/v2/counties.csv?apiKey=0600140b5e8f4e179b6c7fdf39dce72f"
#import pandas as pd
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


def getCSV():
    # Retrieving the data
    req = requests.get(link)
    url_content = req.content
    csv_file = open('counties.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()


def getAllCounties():
    # organizing the data.
    results = []
    file_name = "counties.csv"
    file = open(file_name,'r')
    lines = file.readlines()
    for k in range(0,len(lines),1):
        temp = {}
        arraysplit = lines[k].split(',')
        temp['state'] = arraysplit[2]
        temp['county'] = arraysplit[3]
        temp['population'] = arraysplit[8]
        results.append(temp)
    return results

def getAllStates():
    temp = getAllCounties()
    results = []
    counter = 0
        
    


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




