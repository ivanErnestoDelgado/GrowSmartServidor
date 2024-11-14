from django.urls import path
from .api import *

urlpatterns = [
    path('api/smartpots/create/', SmartPotCreateView.as_view(), name='create_smartpot'),
    path('api/smartpots/', UserSmartPotListView.as_view(), name='user_smartpots'),
    path('api/smartpots/<int:pk>/', SmartPotDetailView.as_view(), name='smartpot_detail'),
    path('api/smartpots/<int:pk>/sensors/', SensorsDataListView.as_view(), name='sensor_data_list'),  # GET para obtener datos
    path('api/smartpots/<int:pk>/sensors/add/', SensorsDataCreateView.as_view(), name='sensor_data_create'),  # POST para registrar datos
     # Configuraciones de macetas
    path('api/smartpots/<int:pk>/configurations/', SmartPotConfigurationsView.as_view(), name='smartpot_configurations'),
    # Riego automático
    path('api/smartpots/<int:pk>/watering/', WateringEventListView.as_view(), name='watering_event_list'),  # GET para historial
    path('api/smartpots/<int:pk>/watering/add/', WateringEventCreateView.as_view(), name='watering_event_create'),  # POST para registrar evento
    path('smartpots/<int:smartpot_id>/alerts/', SmartPotAlertsView.as_view(), name='smartpot-alerts'),
]