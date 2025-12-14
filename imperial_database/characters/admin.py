from django.contrib import admin
from .models import Characters, Starships

# Регистрируем модели, чтобы они появились в админке
admin.site.register(Characters)
admin.site.register(Starships)
