from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from users.models import UserProfile
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from .functions import *
from rest_framework.views import APIView

class SmartPotCreateView(generics.CreateAPIView):
    serializer_class = SmartPotCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        smart_pot=serializer.save(user_profile=UserProfile.objects.get(user=self.request.user))  # Asocia la maceta al usuario autenticado
        obtained_plant=smart_pot.plant

        Configurations.objects.create(
            maximun_temperature=obtained_plant.maximun_temperature,
            minimun_temperature=obtained_plant.minimun_temperature,
            maximun_humidity=obtained_plant.maximun_humidity,
            minimun_humidity=obtained_plant.minimun_humidity,
            maximun_ligth_level=obtained_plant.maximun_ligth_level,
            minimun_ligth_level=obtained_plant.minimun_ligth_level,
            smartpot=smart_pot,
            plant=obtained_plant
        )



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
        return SensorsData.objects.filter(smart_pot__id=smart_pot_id, 
                                          smart_pot__user_profile=UserProfile.objects.get
                                          (user=self.request.user))
    
class SensorsDataCreateView(generics.CreateAPIView):
    serializer_class = SensorsDataSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        smart_pot_id = self.kwargs['pk']
        smart_pot = SmartPot.objects.get(id=smart_pot_id, user_profile=UserProfile.objects.get(user=self.request.user))  # Verifica que la maceta pertenezca al usuario
        sensor_data=serializer.save(smart_pot=smart_pot)
        smart_pot = sensor_data.smart_pot
        plant = smart_pot.plant

        # Se llama a una funcion que retorna la cantidad de limites que se sobrepasaron comparandolo con los datos de los sensores y la planta
        breaked_limits = find_breaked_limits(sensor_data, plant)
        
        obtained_smartpot_status=evaluate_plant_status(len(breaked_limits))
        # Actualiza el estado de la maceta basado en el número de parámetros fuera de los límites
        smart_pot.status=obtained_smartpot_status

        choosed_alert_type=choose_alert_type_from_status_choices(obtained_smartpot_status)
        generated_alert_message=obtain_alert_message(choosed_alert_type,breaked_limits)
        
        Alert.objects.create(alert_type=choosed_alert_type,alert_content=generated_alert_message,smartpot=smart_pot)
        smart_pot.save()

        

class SmartPotConfigurationsView(generics.GenericAPIView):
    serializer_class = ConfigurationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        smart_pot_id = self.kwargs['pk']
        # Verifica que el usuario sea el dueño de la maceta
        configurations = Configurations.objects.filter(smartpot__id=smart_pot_id, smartpot__user_profile=
                                                       UserProfile.objects.get(user=self.request.user)).first()
        if not configurations:
            raise PermissionDenied("No tienes permiso para acceder a esta configuración.")
        return configurations

    def get(self, request, pk):
        # Intenta obtener las configuraciones de la maceta
        configurations = Configurations.objects.filter(smartpot__id=pk, smartpot__user_profile=
                                                       UserProfile.objects.get(user=request.user)).first()
        if configurations:
            serializer = self.get_serializer(configurations)
            return Response(serializer.data)
        else:
            # Devuelve un mensaje indicando que no hay configuraciones aún
            return Response({"detail": "Configuraciones no encontradas. Puedes crearlas usando PUT."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        # Verifica si ya existen configuraciones para esta maceta
        configurations = Configurations.objects.filter(smartpot__id=pk, smartpot__user_profile=
                                                       UserProfile.objects.get(user=request.user)).first()
        if configurations:
            # Si existen, actualiza las configuraciones
            serializer = self.get_serializer(configurations, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            # Si no existen, crea nuevas configuraciones asociadas a la maceta
            smart_pot = SmartPot.objects.get(id=pk, user_profile=UserProfile.objects.get(user=self.request.user))
            associated_plant=smart_pot.plant
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(smartpot=smart_pot,plant=associated_plant)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
class WateringEventCreateView(generics.CreateAPIView):
    serializer_class = WateringEventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        smart_pot_id = self.kwargs['pk']
        smart_pot = SmartPot.objects.get(id=smart_pot_id, user_profile=UserProfile.objects.get(user=self.request.user))  # Verifica que la maceta pertenezca al usuario
        serializer.save(smart_pot=smart_pot)

        obtained_alert_type=Alert.Type.WATHERING_EVENT
        alert_message=obtain_alert_message(obtained_alert_type, [])
        Alert.objects.create(alert_type=obtained_alert_type,alert_content=alert_message,smartpot=smart_pot)


class WateringEventListView(generics.ListAPIView):
    serializer_class = WateringEventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        smart_pot_id = self.kwargs['pk']
        return WateringEvent.objects.filter(smart_pot__id=smart_pot_id, smart_pot__user_profile=UserProfile.objects.get(user=self.request.user))
    
class SmartPotAlertsView(APIView):
    permission_classes = [IsAuthenticated]  # Requiere autenticación

    def get(self, request, smartpot_id):
        try:
            # Filtra el SmartPot por ID y verifica que pertenezca al usuario autenticado
            smartpot = SmartPot.objects.get(id=smartpot_id, user_profile=UserProfile.objects.get(user=self.request.user))
            alerts = Alert.objects.filter(smartpot=smartpot)
            serializer = AlertSerializer(alerts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SmartPot.DoesNotExist:
            return Response({"error": "SmartPot not found or access denied"}, status=status.HTTP_404_NOT_FOUND)