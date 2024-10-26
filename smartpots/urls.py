from django.urls import path
from .api import SmartPotCreateView, UserSmartPotListView,SmartPotDetailView,SensorsDataCreateView,SensorsDataListView

urlpatterns = [
    path('api/smartpots/create/', SmartPotCreateView.as_view(), name='create_smartpot'),
    path('api/smartpots/', UserSmartPotListView.as_view(), name='user_smartpots'),
    path('api/smartpots/<int:pk>/', SmartPotDetailView.as_view(), name='smartpot_detail'),
    path('api/smartpots/<int:pk>/sensors/', SensorsDataListView.as_view(), name='sensor_data_list'),  # GET para obtener datos
    path('api/smartpots/<int:pk>/sensors/add/', SensorsDataCreateView.as_view(), name='sensor_data_create'),  # POST para registrar datos
]