from django.db import models


class Characters(models.Model):
    name = models.CharField(max_length=100, unique=True)
    height = models.CharField(max_length=10, default='не известно')
    mass = models.CharField(max_length=10, default='не известно')
    hair_color = models.CharField(max_length=50, default='не известно')
    skin_color = models.CharField(max_length=50, default='не известно')
    eye_color = models.CharField(max_length=50, default='не известно')
    birth_year = models.CharField(max_length=20, default='не известно')
    gender = models.CharField(max_length=20, default='не известно')

    def __str__(self):
        return self.name


class Starships(models.Model):
    name = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=100, default='не известно')
    manufacturer = models.CharField(max_length=150, default='не известно')
    cost_in_credits = models.CharField(max_length=20, default='не известно')
    length = models.CharField(max_length=20, default='не известно')
    crew = models.CharField(max_length=20, default='не известно')
    passengers = models.CharField(max_length=20, default='не известно')

    def __str__(self):
        return self.name
