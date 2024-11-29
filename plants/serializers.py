from rest_framework import serializers
from .models import *


class PlantRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlantRecomendation
        fields=(
            'type',
            'content'
        )

#Serializador del modelo de Plants
class PlantSerializer(serializers.ModelSerializer):
    recommendations=PlantRecommendationSerializer(many=True, read_only=True)
    class Meta:
        model=Plant
        fields=(
            'id',
            'name',
            'maximun_temperature',
            'minimun_temperature',
            'maximun_humidity',
            'minimun_humidity',
            'maximun_ligth_level',
            'minimun_ligth_level',
            'created_at',
            'updated_at',
            'recommendations'
        )
        read_only_fields=('created_at',)


class PlantWithRecommendationsSerializer(serializers.ModelSerializer):
    recommendations = PlantRecommendationSerializer(many=True, read_only=True)
    class Meta:
        model = Plant
        fields = ['id', 'name', 'recommendations']
