import requests
from concurrent.futures import ThreadPoolExecutor

base_url ="https://pokeapi.co/api/v2"

#test if searching up by pokemon name worked
def search_pokemon_name(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")
        
def search_pokemon_species(name):
    url = f"{base_url}/pokemon-species/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

def get_pokemon_data(name):
    with ThreadPoolExecutor() as executor:
        info_future = executor.submit(search_pokemon_name, name)
        species_future = executor.submit(search_pokemon_species, name)
        info = info_future.result()
        species = species_future.result()
    if info:
        return info, None
    elif species:
        return None, species
    else:
        return None, None

pokemon_name = input("Search up Pokemon name: ")
pokemon_info, pokemon_species = get_pokemon_data(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"Pokedex #: {pokemon_info["id"]}")
    # print(f"{pokemon_info["height"]}")
elif pokemon_species:
    print(f"Name: {pokemon_species["name"].capitalize()}")
    print(f"Pokedex #: {pokemon_species["id"]}")
else:
    print("Pokemon not found.")