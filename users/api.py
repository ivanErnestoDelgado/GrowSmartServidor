from rest_framework import generics,status
from .serializers import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import authenticate

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializer.data,
            "message": "Usuario registrado correctamente"
        }, status=status.HTTP_201_CREATED)

class CustomAuthToken(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Obtiene o crea el token
            token, created = Token.objects.get_or_create(user=user)
            # Serializa los datos del usuario y su perfil
            user_data = UserSerializer(user).data
            # Agrega el token a la respuesta
            return Response({
                'token': token.key,
                'user': user_data
            })
        else:
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_400_BAD_REQUEST)
        
class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Se ha enviado un correo para restablecer la contraseña."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]  # Asegurar que solo usuarios autenticados accedan

    def put(self, request, *args, **kwargs):
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return Response({"error": "Perfil no encontrado o no autorizado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileSerializer(instance=profile, data=request.data, partial=True)  # Permitir actualizaciones parciales
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            # Cambiar la contraseña del usuario
            request.user.set_password(serializer.validated_data['new_password'])
            request.user.save()
            return Response({"message": "La contraseña ha sido cambiada exitosamente."}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)