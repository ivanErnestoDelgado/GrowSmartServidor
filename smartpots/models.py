from django.db import models
from plants.models import Plant
from users.models import UserProfile
from django.utils import timezone

# Create your models here.

class SmartPot(models.Model):
    INACTIVE = 0
    GOOD = 1
    WARNING = 2
    DANGER = 3

    STATUS_CHOICES = [
        (INACTIVE, 'Inactivo'),
        (GOOD, 'Bueno'),
        (WARNING, 'Advertencia'),
        (DANGER, 'En peligro')
    ]
    serial_number=models.CharField(max_length=50)
    pot_name=models.CharField(max_length=100)
    ubication=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now=True)
    size=models.CharField(max_length=40)
    status=models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=INACTIVE)
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
   light_level=models.PositiveIntegerField()
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

class Alert(models.Model):
    class Type(models.TextChoices):
        WATHERING_EVENT = 'eventoRiego', 'Evento de Riego'
        OUT_OF_DANGER = 'peligroNulo', 'Peligro Nulo'
        MODERATE_DANGER = 'peligroModerado', 'Peligro Moderado'
        HIGH_DANGER = 'peligroAlto', 'Peligro Alto'

    alert_type = models.CharField(
        max_length=20,
        choices=Type.choices,
        default=Type.OUT_OF_DANGER,
    )
    alert_content = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    smartpot = models.ForeignKey(SmartPot, on_delete=models.CASCADE, related_name='alerts')

    def __str__(self):
        return f"{self.alert_type} - {self.alert_content[:30]}"