from django.db import models
from plants.models import Plant
from users.models import UserProfile

# Create your models here.

class SmartPot(models.Model):
    pot_name=models.CharField(max_length=100)
    ubication=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now=True)
    user_profile= models.ForeignKey(UserProfile, related_name='smartpots', on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, related_name='smartpots', on_delete=models.CASCADE)

    def __str__(self):
     return f'{self.pot_name}-{self.user_profile.user.username}'
 

class WateringEvent(models.Model):
   water_amount=models.PositiveIntegerField()
   watering_date=models.DateTimeField(auto_now=True)
   smart_pot=models.ForeignKey(SmartPot,related_name='wateringEvents',on_delete=models.CASCADE)

class SensorsData(models.Model):
   floor_humidity=models.DecimalField(max_digits=5, decimal_places=2)
   temperature=models.PositiveIntegerField()
   ligth_level=models.PositiveIntegerField()
   water_level=models.PositiveIntegerField()
   registed_at=models.DateTimeField(auto_now=True)
   smart_pot=models.ForeignKey(SmartPot, related_name='SensorsData', on_delete=models.CASCADE)

class Configurations(models.Model):
   maximun_temperature = models.DecimalField(max_digits=5, decimal_places=2)  # Temperatura maxima
   minimun_temperature = models.DecimalField(max_digits=5, decimal_places=2,)  # Temperatura minima
   maximun_humidity = models.DecimalField(max_digits=5, decimal_places=2)  # Nivel de humedad maximo
   minumun_humidity = models.DecimalField(max_digits=5, decimal_places=2)  # Nivel de humedad minimo
   maximun_ligth_level=models.PositiveIntegerField() # Nivel de luz maximo
   minimun_ligth_level=models.PositiveIntegerField()   # Nivel de humedad minimo
   notifications_is_activated=models.BooleanField()
   smartpot=models.ForeignKey(SmartPot, related_name='smartpot', on_delete=models.CASCADE)
   plant=models.ForeignKey(Plant, related_name='plant', on_delete=models.CASCADE)

