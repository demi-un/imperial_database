from django.shortcuts import render, get_object_or_404
from .models import Characters, Starships


def index(request):
    characters = Characters.objects.all()
    return render(request, 'characters/index.html', {'characters': characters})


def show_person(request, person_name):
    person = get_object_or_404(Characters, name=person_name)

    context = {
        'person': person,
        'starships': person.starships.all()
    }

    return render(request, 'characters/person.html', context)


def show_starship(request, starship_name):
    starship = get_object_or_404(Starships, name=starship_name)
    return render(request, 'characters/starship.html', {'starship': starship})
