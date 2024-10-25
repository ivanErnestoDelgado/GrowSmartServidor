from django.urls import path
from .api import SmartPotCreateView, UserSmartPotListView,SmartPotDetailView

urlpatterns = [
    path('api/smartpots/create/', SmartPotCreateView.as_view(), name='create_smartpot'),
    path('api/smartpots/', UserSmartPotListView.as_view(), name='user_smartpots'),
    path('api/smartpots/<int:pk>/', SmartPotDetailView.as_view(), name='smartpot_detail'),
]