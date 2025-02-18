##weather_report gave trouble, also encoded, seeing if this one is easier to start with
##import requests gives trouble, module not found even after installing
##with py -m pip install requests: no module named pip. weird?
# Python version: 3.13.1. pip 25.0, pip lists shows requests.
# Think it has to do with where everything is installed, but dont know how to fix that
# uv pip install requests does seem to do something as now I can see it in the venv

# API key: 4dba58d15a
# example request: https://weerlive.nl/api/weerlive_api_v2.php?key=4dba58d15a&locatie=Amsterdam

import requests

#test = "https://weerlive.nl/api/weerlive_api_v2.php?key=4dba58d15a&locatie=Amsterdam"

base_url = "https://weerlive.nl/api/weerlive_api_v2.php"

key = "4dba58d15a"
plaatsnaam = "Amsterdam"
# Get different responses with placenames, but also get responses with random strings. How to check if its an actual hit?

params = {"locatie": plaatsnaam, "key": key}

def get_weather_info(params):
    response = requests.get(base_url, params = params)
    if response.status_code == 200:
        weather_data = response.json()
        #print(weather_data)
        return weather_data
    else:
        print(f"failed to retrieve data {response.status_code}")


weather_report = get_weather_info(params)

if liveweer := weather_report.get("liveweer"):
    print(f"{liveweer[0]['plaats']}")
    print(
        f"Het is {liveweer[0]['temp']} graden, maar het voelt als {liveweer[0]['gtemp']}"
    )
    print(f"Het weer: {liveweer[0]['samenv']}")
    print(f"Verwachting: {liveweer[0]['verw']}")
    print(f"Waarschuwingen: {liveweer[0]['ltekst']}")
