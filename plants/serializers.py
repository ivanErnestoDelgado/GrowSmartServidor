from rest_framework import serializers
from .models import Plant

#Serializador del modelo de Plants
class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plant
        fields=(
            'id',
            'name',
            'scientific_name',
            'description',
            'ideal_temperature',
            'ideal_humidity',
            'sunlight_needs',
            'watering_frequency',
            'created_at',
            'updated_at'
        )
        read_only_fields=('created_at',)

