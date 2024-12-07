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
    recommendations=PlantRecommendationSerializer(many=True)
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
        
    def create(self, validated_data):
        # Extraer recomendaciones del dato validado
        recommendations_data = validated_data.pop('recommendations')
        
        # Crear la planta
        plant = Plant.objects.create(**validated_data)

        # Crear las recomendaciones asociadas a la planta
        for recommendation_data in recommendations_data:
            PlantRecomendation.objects.create(plant=plant, **recommendation_data)

        return plant

class PlantWithRecommendationsSerializer(serializers.ModelSerializer):
    recommendations = PlantRecommendationSerializer(many=True, read_only=True)
    class Meta:
        model = Plant
        fields = ['id', 'name', 'recommendations']
