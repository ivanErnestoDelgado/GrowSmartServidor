from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Plant
from .serializers import *
from rest_framework.permissions import IsAuthenticated

class PlantListView(APIView):
    def get(self, request):
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlantDetailWithRecommendationsView(generics.RetrieveAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantWithRecommendationsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
