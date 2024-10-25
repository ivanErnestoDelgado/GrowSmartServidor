from django.urls import path
from .api import RegisterView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('api/users/register/', RegisterView.as_view(), name='register'),
    path('api/users/login/', obtain_auth_token, name='login'),
]

