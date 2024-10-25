from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import SmartPot
from .serializers import SmartPotCreateSerializer,SmartPotSerializer
from users.models import UserProfile
class SmartPotCreateView(generics.CreateAPIView):
    serializer_class = SmartPotCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_profile=UserProfile.objects.get(user=self.request.user))  # Asocia la maceta al usuario autenticado


class UserSmartPotListView(generics.ListAPIView):
    serializer_class = SmartPotSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SmartPot.objects.filter(user_profile=UserProfile.objects.get(user=self.request.user))