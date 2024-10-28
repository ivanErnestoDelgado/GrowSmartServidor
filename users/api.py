from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status

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
