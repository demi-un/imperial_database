import requests
from .models import Starships, Characters


def get_data(url):
    data_list = []
    while url:
        response = requests.get(url).json()
        data_list.extend(response["results"])
        url = response["next"]
    return data_list


def load_starships():
    starships_list = get_data("https://swapi.dev/api/starships/")

    for starship in starships_list:
        Starships.objects.create(
            name=starship["name"],
            model=starship["model"],
            manufacturer=starship["manufacturer"],
            cost_in_credits=starship["cost_in_credits"],
            length=starship["length"],
            crew=starship["crew"],
            passengers=starship["passengers"]
        )


def load_characters():
    characters_list = get_data("https://swapi.dev/api/people/")

    for person in characters_list:
        Characters.objects.create(
            name=person["name"],
            height=person["height"],
            mass=person["mass"],
            hair_color=person["hair_color"],
            skin_color=person["skin_color"],
            eye_color=person["eye_color"],
            birth_year=person["birth_year"],
            gender=person["gender"]
        )
