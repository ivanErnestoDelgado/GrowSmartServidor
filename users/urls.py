from django.urls import path
from .api import RegisterView

urlpatterns = [
    path('api/users/register/', RegisterView.as_view(), name='register'),
]