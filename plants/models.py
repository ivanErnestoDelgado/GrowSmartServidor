from django.db import models
# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)  # Nombre casual de la planta
    maximun_temperature = models.DecimalField(max_digits=5, decimal_places=2)  # Temperatura maxima
    minimun_temperature = models.DecimalField(max_digits=5, decimal_places=2,)  # Temperatura minima
    maximun_humidity = models.DecimalField(max_digits=5, decimal_places=2)  # Nivel de humedad maximo
    minumun_humidity = models.DecimalField(max_digits=5, decimal_places=2)  # Nivel de humedad minimo
    maximun_ligth_level=models.PositiveIntegerField() # Nivel de luz maximo
    minimun_ligth_level=models.PositiveIntegerField()   # Nivel de humedad minimo
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    plant_cares=models.TextField()
    def __str__(self):
        return self.name

#ACTUALIZAR EL SERIALIZER DESPUES