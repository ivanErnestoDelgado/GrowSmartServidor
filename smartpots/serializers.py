from rest_framework import serializers
from .models import *
from plants.serializers import PlantSerializer
#Serializador de los modelos
class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Configurations
        fields=(
            'id',
            'maximun_temperature',
            'minimun_temperature',
            'maximun_humidity',
            'minimun_humidity',
            'maximun_ligth_level',
            'minimun_ligth_level',
            'notifications_is_activated'
        )

class SmartPotSerializer(serializers.ModelSerializer):
    plant=PlantSerializer()
    class Meta:
        model=SmartPot
        fields=(
            'id',
            'serial_number',
            'pot_name',
            'ubication',
            'updated_at',
            'size',
            'status',
            'plant'
        )
        

class WateringEventSerializer(serializers.ModelSerializer):
    class Meta:
        model=WateringEvent
        fields=(
            'id',
            'water_amount',
            'watering_date'
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
            'registed_at'
        )

#Modelos para las operaciones con los modelos
class SmartPotCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartPot
        fields = [  'serial_number',
                    'pot_name',
                    'ubication',
                    'updated_at',
                    'size',
                    'plant']
        extra_kwargs = {'plant': {'write_only': True}}  # El ID de la planta se envía en la creación

    def to_representation(self, instance):
        # Usamos el `SmartPotSerializer` para la representación final
        return SmartPotSerializer(instance).data
    
class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['id','alert_type', 'alert_content', 'create_time', 'smartpot']