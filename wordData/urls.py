from django.urls import path
from . import views
from rest_framework.views import APIView
from django.contrib.auth import views as auth_views
from .views import transfer_vocabulary

urlpatterns = [
    path('transfer_vocabulary/', transfer_vocabulary, name='transfer_vocabulary'),
]

