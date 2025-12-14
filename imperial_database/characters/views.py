from django.shortcuts import render, get_object_or_404
from .models import Characters, Starships


def index(request):
    characters = Characters.objects.all()
    return render(request, 'characters/index.html', {'characters': characters})


def show_person(request, person_slug):
    person = get_object_or_404(Characters, slug=person_slug)

    context = {
        'person': person,
        'starships': person.starships.all()
    }

    return render(request, 'characters/person.html', context)


def show_starship(request, person_slug, starship_slug):
    person = get_object_or_404(Characters, slug=person_slug)
    starship = get_object_or_404(person.starships, slug=starship_slug)

    context = {
        "person": person,
        "starship": starship,
    }

    return render(request, 'characters/starship.html', context)
