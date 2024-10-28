from django.contrib import admin
from django.apps import apps

# Register your models here.

# Obtiene todos los modelos de la aplicación actual y los registra en el admin
app = apps.get_app_config('plants')  # Reemplaza con el nombre de tu aplicación
for model in app.get_models():
    admin.site.register(model) 