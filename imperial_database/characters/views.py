from django.shortcuts import render


def index(request):
    return render(request, 'characters/index.html')


def show_person(request, person_name):
    data = {
        'title': f'Страница корабля {person_name}'
    }

    return render(request, 'characters/person.html', data)


def show_starship(request, starship_name):
    data = {
        'title': f'Страница корабля {starship_name}'
    }

    return render(request, 'characters/starship.html', data)
