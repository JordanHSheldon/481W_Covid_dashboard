import urllib.request, json 

# function for specific state info
def getStateInfo(State):
    with urllib.request.urlopen("https://api.covidtracking.com/v1/states/mi/current.json") as url:
        data = json.loads(url.read().decode())
        print(data['state'])
        print(data['positive'])
        print(data['positiveIncrease'])
        print(data['deathIncrease'])
        print(data['deathConfirmed'])
        print(data)


# function for all state info  
def getAllStateInfo():  
    with urllib.request.urlopen("https://api.covidtracking.com/v1/states/current.json") as url:
        data = json.loads(url.read().decode())
        print(data)