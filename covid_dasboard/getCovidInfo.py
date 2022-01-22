from sre_parse import State
import urllib.request, json 

# function for specific state info
def getStateInfo(State):
    with urllib.request.urlopen("https://api.covidtracking.com/v1/states/mi/current.json") as url:
        data = json.loads(url.read().decode())
        return(data)


# function for all state info  
def getAllStateInfo():  
    with urllib.request.urlopen("https://api.covidtracking.com/v1/states/current.json") as url:
        data = json.loads(url.read().decode())
        print(data[3])
        return(data)