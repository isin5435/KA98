from django.urls import path
from . import views
from rest_framework.views import APIView
from django.contrib.auth import views as auth_views
from .views import transfer_vocabulary, userWord_list, word_list, WordLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('', views.word_list, name="word"),
    path('', WordLoginView.as_view(), name='word'),
    path('transfer_vocabulary/', transfer_vocabulary, name='transfer_vocabulary'),
    path('delete_word/<int:vocab_id>/', views.delete_word, name='delete_word'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

