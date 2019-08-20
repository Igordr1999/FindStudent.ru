from django.urls import path
from . import views
from rest_framework.authtoken import views as drf

urlpatterns = [
    path('api-token-auth/', drf.obtain_auth_token)
]
