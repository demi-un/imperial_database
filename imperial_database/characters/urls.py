from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path('<str:person_name>/', views.show_person, name='show_person'),
    path('starship/<str:starship_name>/', views.show_starship, name='show_starship')
]
