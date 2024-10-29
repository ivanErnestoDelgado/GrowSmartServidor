from rest_framework import serializers
from .models import *

#Serializador del modelo de Plants
class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plant
        fields=(
            'id',
            'name',
            'maximun_temperature',
            'minimun_temperature',
            'maximun_humidity',
            'minumun_humidity',
            'maximun_ligth_level',
            'minimun_ligth_level',
            'created_at',
            'updated_at'
        )
        read_only_fields=('created_at',)


class PlantRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlantRecomendation
        fields=(
            'type',
            'recommendation'
        )

class PlantWithRecommendationsSerializer(serializers.ModelSerializer):
    recommendations = PlantRecommendationSerializer(many=True, read_only=True)
    class Meta:
        model = Plant
        fields = ['id', 'name', 'recommendations']
