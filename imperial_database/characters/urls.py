from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path('<slug:person_slug>/', views.show_person, name='show_person'),
    path('<slug:person_slug>/<slug:starship_slug>/', views.show_starship, name='show_starship')
]
