from django.db import models
from enum import Enum
# Create your models here.
class Plant(models.Model):
    class dataStatusFromSensor(Enum):
        LOWER=0
        NORMAL=1
        HIGHER=2

    name = models.CharField(max_length=100)  # Nombre casual de la planta
    maximun_temperature = models.DecimalField(max_digits=5, decimal_places=2)  # Temperatura maxima
    minimun_temperature = models.DecimalField(max_digits=5, decimal_places=2,)  # Temperatura minima
    maximun_humidity = models.DecimalField(max_digits=5, decimal_places=2)  # Nivel de humedad maximo
    minimun_humidity = models.DecimalField(max_digits=5, decimal_places=2)  # Nivel de humedad minimo
    maximun_ligth_level=models.PositiveIntegerField() # Nivel de luz maximo
    minimun_ligth_level=models.PositiveIntegerField()   # Nivel de luz minimo
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    
    def evaluate_light_data(self,sensor_light_data):
        return self.obtain_data_status(sensor_light_data,self.minimun_ligth_level,self.maximun_ligth_level)

    def evaluate_temperature_data(self, sensor_temperature_data):
        return self.obtain_data_status(sensor_temperature_data,self.minimun_temperature,self.maximun_temperature)
    
    def evaluate_humidity_data(self, sensor_humidity_data):
        return self.obtain_data_status(sensor_humidity_data,self.minimun_humidity,self.maximun_humidity)
    
    def obtain_data_status(self,sensor_data,minimun,maximun):
        if(sensor_data<minimun):
            return self.dataStatusFromSensor.LOWER
        if(sensor_data>maximun):
            return self.dataStatusFromSensor.HIGHER
        return self.dataStatusFromSensor.NORMAL

class PlantRecomendation(models.Model):
    class RecommendationType(models.TextChoices):
        POSITIVE = 'positive', 'Positive'
        NEGATIVE = 'negative', 'Negative'

    
    type = models.CharField(
        max_length=8,
        choices=RecommendationType.choices,
        default=RecommendationType.POSITIVE
    )
    content = models.CharField(max_length=255)
    plant = models.ForeignKey(Plant, related_name='recommendations', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.type} - {self.content}"  # Muestra el tipo y los primeros caracteres de la recomendación
