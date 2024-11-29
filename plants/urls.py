from .api import *
from django.urls import path

urlpatterns = [
     path('api/plants/<int:id>/recommendations/', PlantDetailWithRecommendationsView.as_view(), name='plant_care'),
     path('api/plants',PlantListView.as_view(), name='plants'),
]
