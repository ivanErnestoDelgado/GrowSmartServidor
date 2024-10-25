from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  #

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Serializamos el campo 'user' utilizando un serializer aparte

    class Meta:
        model = UserProfile
        fields = ['user', 'location', 'phone_number', 'bio', 'created_at']
        read_only_fields = ['created_at']  # 'created_at' solo es de lectura