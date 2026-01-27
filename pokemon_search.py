import requests
from concurrent.futures import ThreadPoolExecutor

base_url ="https://pokeapi.co/api/v2"

#test if searching up by pokemon name worked
def search_pokemon_name(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
#test if searching up by pokemon species worked
def search_pokemon_species(name):
    url = f"{base_url}/pokemon-species/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

#call both api requests at the same time
def get_pokemon_data(user_input):
    with ThreadPoolExecutor() as executor:
        name_future = executor.submit(search_pokemon_name, user_input)
        species_future = executor.submit(search_pokemon_species, user_input)
        name = name_future.result()
        species = species_future.result()
    #runs if searching up by the pokemon name was successful
    if name:
        return name, None
    ##runs if searching up by the pokemon name fails, but the species was found
    elif species:
        return None, species
    #if both name and species fail
    else:
        return None, None

#user is asked to enter Pokemon name
while True:
    pokemon_name = input("Search up Pokemon: ")
    pokemon_info, pokemon_species = get_pokemon_data(pokemon_name)

    if pokemon_info:
        print(f"Name: {pokemon_info['name'].capitalize()}")
        print(f"Pokedex #: {pokemon_info['id']}")
        # print(f"{pokemon_info["height"]}")
    elif pokemon_species:
        print(f"Name: {pokemon_species['name'].capitalize()}")
        print(f"Pokedex #: {pokemon_species['id']}")
    else:
        print("Pokemon not found.")
