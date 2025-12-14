import requests
from .models import Starships, Characters


def get_data(url):
    data_list = []
    while url:
        response = requests.get(url).json()
        data_list.extend(response["results"])
        url = response["next"]
    return data_list


starships_list = get_data("https://swapi.dev/api/starships/")
characters_list = get_data("https://swapi.dev/api/people/")


def load_starships():
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


def load_connection():
    # {starship_url: starship_name}
    starships_by_url = {
        starship["url"]: starship["name"] for starship in starships_list
    }

    # {starship_name: Starships.object}
    starships_db = {
        starship.name: starship for starship in Starships.objects.all()
    }

    for person in characters_list:
        # проверка: есть ли корабли
        if not person["starships"]:
            continue

        character = Characters.objects.get(name=person["name"])

        for starship_url in person["starships"]:
            starship_name = starships_by_url.get(starship_url)

            starship = starships_db.get(starship_name)
            character.starships.add(starship)
