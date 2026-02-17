import requests
from concurrent.futures import ThreadPoolExecutor
from django.shortcuts import render

BASE_URL = "https://pokeapi.co/api/v2"


def search_pokemon_name(name):
    url = f"{BASE_URL}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def search_pokemon_species(name):
    url = f"{BASE_URL}/pokemon-species/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def get_pokemon_data(user_input):
    with ThreadPoolExecutor() as executor:
        name_future = executor.submit(search_pokemon_name, user_input)
        species_future = executor.submit(search_pokemon_species, user_input)
        name_result = name_future.result()
        species_result = species_future.result()

    if name_result:
        return name_result, None
    elif species_result:
        return None, species_result
    else:
        return None, None


def index(request):
    context = {}
    query = request.GET.get("q", "").strip()

    if query:
        context["query"] = query
        pokemon_info, pokemon_species = get_pokemon_data(query.lower())

        if pokemon_info:
            context["pokemon"] = {
                "name": pokemon_info["name"].capitalize(),
                "pokedex_number": pokemon_info["id"],
                "sprite": pokemon_info["sprites"]["front_default"],
                "types": [t["type"]["name"].capitalize() for t in pokemon_info["types"]],
                "height": pokemon_info["height"] / 10,  # convert to meters
                "weight": pokemon_info["weight"] / 10,  # convert to kg
            }
        elif pokemon_species:
            # Species endpoint doesn't have sprites, so fetch the pokemon data using the species id
            pokemon_info = search_pokemon_name(str(pokemon_species["id"]))
            sprite = pokemon_info["sprites"]["front_default"] if pokemon_info else None
            types = [t["type"]["name"].capitalize() for t in pokemon_info["types"]] if pokemon_info else []
            height = pokemon_info["height"] / 10 if pokemon_info else None
            weight = pokemon_info["weight"] / 10 if pokemon_info else None

            context["pokemon"] = {
                "name": pokemon_species["name"].capitalize(),
                "pokedex_number": pokemon_species["id"],
                "sprite": sprite,
                "types": types,
                "height": height,
                "weight": weight,
            }
        else:
            context["error"] = "Pokemon not found."

    return render(request, "search/index.html", context)
