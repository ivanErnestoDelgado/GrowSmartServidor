from rest_framework import serializers
from .models import Configurations,SensorsData,SmartPot,WateringEvent

#Serializador del modelo de Plants
class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Configurations
        fields=(
            'id',
            'maximun_temperature',
            'minimun_temperature',
            'maximun_humidity',
            'minumun_humidity',
            'maximun_ligth_level',
            'minimun_ligth_level',
            'notifications_is_activated',
            'smartpot',
            'plant'
        )

class SmartPotSerializer(serializers.ModelSerializer):
    class Meta:
        model=SmartPot
        fields=(
            'id',
            'pot_name',
            'ubication',
            'updated_at',
            'user_profile',
            'plant'
        )

class WateringEventSerializer(serializers.ModelSerializer):
    class Meta:
        model=WateringEvent
        fields=(
            'id',
            'water_amount',
            'watering_date',
            'smart_pot'
        )

class SensorsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=SensorsData
        fields=(
            'id',
            'floor_humidity',
            'temperature',
            'light_level',
            'water_level',
            'registed_at',
            'smart_pot'
        )