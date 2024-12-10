from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User
from random import choice
import string

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        read_only_fields=['id']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Serializamos el campo 'user' utilizando un serializer aparte

    class Meta:
        model = UserProfile
        fields = ['user', 'location', 'phone_number', 'bio', 'created_at']
        read_only_fields = ['created_at']  # 'created_at' solo es de lectura
    def update(self, instance, validated_data):
            # Extraer los datos de 'user'
        user_data = validated_data.pop('user', None)

            # Actualizar los datos del modelo User
        if user_data:
            user_instance = instance.user  # Relación OneToOne con User
            for attr, value in user_data.items():
                setattr(user_instance, attr, value)  # Actualiza los atributos del modelo User
            user_instance.save()

            # Actualizar los datos del modelo UserProfile
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance  
        
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
    
class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    generated_password = ''.join(choice(string.ascii_letters + string.digits) for _ in range(8))
    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("No existe un usuario con este correo electrónico.")
        return value

    def save(self):
        email = self.validated_data['email']
        user = User.objects.get(email=email)
        user.set_password(self.generated_password)
        user.save()

            # Enviar el correo (puedes personalizar el contenido)
        user.email_user(
            subject="Restablecimiento de contraseña",
            message=f"""
            Hola {user.username},

            Tu nueva contraseña es: {self.generated_password}

            Por favor, cámbiala después de iniciar sesión.

            Saludos,
            El equipo de soporte
            """)

class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)
    
    def validate_current_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("La contraseña actual es incorrecta.")
        return value

    def validate_new_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("La nueva contraseña debe tener al menos 8 caracteres.")
        return value