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
    def __str__(self):
        return self.name


class PlantRecomendation(models.Model):
    class RecommendationType(models.TextChoices):
        POSITIVE = 'positive', 'Positive'
        NEGATIVE = 'negative', 'Negative'

    
    type = models.CharField(
        max_length=8,
        choices=RecommendationType.choices,
        default=RecommendationType.POSITIVE
    )
    recommendation = models.CharField(max_length=255)
    plant = models.ForeignKey(Plant, related_name='recommendations', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.type} - {self.recommendation}"  # Muestra el tipo y los primeros caracteres de la recomendación
