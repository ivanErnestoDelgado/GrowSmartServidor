from django.db import models
# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)  # Nombre casual de la planta
    scientific_name = models.CharField(max_length=100, blank=True, null=True)  # Nombre científico
    description = models.TextField(blank=True, null=True)  # Descripción de la planta
    ideal_temperature = models.DecimalField(max_digits=5, decimal_places=2)  # Temperatura ideal
    ideal_humidity = models.DecimalField(max_digits=5, decimal_places=2)  # Nivel de humedad ideal (%)
    sunlight_needs = models.CharField(max_length=100)  #  Tipo de exposicion a la luz solar (ej. "Directa", "Sombra")
    watering_frequency = models.PositiveIntegerField()  # Frecuencia de riego en días
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

clas