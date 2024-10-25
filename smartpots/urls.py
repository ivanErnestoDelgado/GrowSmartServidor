from django.urls import path
from .api import SmartPotCreateView, UserSmartPotListView

urlpatterns = [
    path('api/smartpots/create/', SmartPotCreateView.as_view(), name='create_smartpot'),
    path('api/smartpots/', UserSmartPotListView.as_view(), name='user_smartpots'),
]