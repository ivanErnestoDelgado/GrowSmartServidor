from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import SmartPot,SensorsData
from .serializers import SmartPotCreateSerializer,SmartPotSerializer,SensorsDataSerializer
from users.models import UserProfile
from rest_framework.exceptions import PermissionDenied

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

class SmartPotDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SmartPot.objects.all()
    serializer_class = SmartPotCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Obtenemos la maceta por ID y verificamos que pertenezca al usuario autenticado
        obj = super().get_object()
        if obj.user_profile != UserProfile.objects.get(user=self.request.user):
            raise PermissionDenied("No tienes permiso para modificar esta maceta.")
        return obj

class SensorsDataListView(generics.ListAPIView):
    serializer_class = SensorsDataSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        smart_pot_id = self.kwargs['pk']
        # Filtra los datos de sensores solo para la maceta especificada y el usuario autenticado
        return SensorsData.objects.filter(smart_pot__id=smart_pot_id, smart_pot__user_profile=UserProfile.objects.get(user=self.request.user))
    
class SensorsDataCreateView(generics.CreateAPIView):
    serializer_class = SensorsDataSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        smart_pot_id = self.kwargs['pk']
        smart_pot = SmartPot.objects.get(id=smart_pot_id, user_profile=UserProfile.objects.get(user=self.request.user))  # Verifica que la maceta pertenezca al usuario
        serializer.save(smart_pot=smart_pot)