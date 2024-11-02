from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True, null=True)  # Ubicación geográfica del usuario
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Número de teléfono opcional
    bio = models.TextField(blank=True, null=True)  # Información adicional del usuario
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username