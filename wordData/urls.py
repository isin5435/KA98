from django.urls import path
from . import views
from rest_framework.views import APIView
from django.contrib.auth import views as auth_views
from .views import transfer_vocabulary, word_list, WordLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('',auth_views.LoginView.as_view(template_name='Project/Word.html'),name='word'),
    path('', WordLoginView.as_view(), name='word'),
    path('transfer_vocabulary/', transfer_vocabulary, name='transfer_vocabulary'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

