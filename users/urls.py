from django.urls import path
from .api import *


urlpatterns = [
    path('api/users/register/', RegisterView.as_view(), name='register'),
    path('api/users/login/', CustomAuthToken.as_view(), name='login'),
    path('api/users/password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('api/users/userprofile/', UserProfileUpdateView.as_view(), name='userprofile_update'),
    path('api/users/change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('api/users/save-fcm-token/', SaveFCMTokenView.as_view(), name='save_fcm_token'),
]

