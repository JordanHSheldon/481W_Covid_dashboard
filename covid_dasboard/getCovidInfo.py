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
        results.append(d)
    formatted_results=[]
    k = 0
    while(k<len(lines)):
        if(results[k]['state']==str(state).upper()):
            formatted_results.append(results[k])
        k+=1
    return formatted_results   
    


# function that returns a counties data and returns it in the 
# form of an array
def getCounty(state,county):
    temp = getState(state)
    for k in range(0,len(temp),1):
        if(temp[k]['county']==county):
            return temp[k]

# function for getting which state is which rank in most covid cases.
def getCovidRank():
    return None




