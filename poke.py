#tutotial

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_poke_info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        poke_data = response.json()
        return poke_data
    else:
        print(f"failed to retrieve data {response.status_code}")

poke_name = "bulbasaur"

poke_info = get_poke_info(poke_name)

if poke_info:
    print(f"Name: {poke_info["name"].capitalize()}")
    print(f"id: {poke_info["id"]}")
    print(f"Height: {poke_info["height"]}")
    print(f"Weight: {poke_info["weight"]}")