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

class RegisterSerializer(serializers.ModelSerializer):
    # Campos adicionales para la información del perfil
    location = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'location', 'phone_number', 'bio']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Extraemos los datos relacionados con el perfil
        profile_data = {
            'location': validated_data.pop('location', ''),
            'phone_number': validated_data.pop('phone_number', ''),
            'bio': validated_data.pop('bio', '')
        }

        # Creamos el usuario
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Creamos el perfil de usuario asociado
        UserProfile.objects.create(user=user, **profile_data)

        return user