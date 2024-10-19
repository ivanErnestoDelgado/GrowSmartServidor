from rest_framework import viewsets,permissions
from .models import Plant
from .serializers import PlantSerializer

class PlantViewSet(viewsets.ModelViewSet):
    queryset= Plant.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=PlantSerializer