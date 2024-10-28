from rest_framework import viewsets,permissions,generics
from .models import Plant
from .serializers import *
from rest_framework.permissions import IsAuthenticated

class PlantView(generics.RetrieveAPIView):
    queryset= Plant.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=PlantSerializer


class PlantCareView(generics.RetrieveAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantCareSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'