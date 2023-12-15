from django.urls import path
from . import views
from rest_framework.views import APIView
from django.contrib.auth import views as auth_views
from .views import transfer_vocabulary

urlpatterns = [
    path('', views.word_list, name="home"),
    path('Word/', auth_views.LoginView.as_view(template_name='Project/chapter.html'), name="room"),
    path('transfer_vocabulary/', transfer_vocabulary, name='transfer_vocabulary'),
]

