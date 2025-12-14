from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:person_name>/', views.show_person),
    path('starship/<slug:starship_name>/', views.show_starship)
]
