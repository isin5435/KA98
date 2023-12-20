from django.urls import path
from . import views
from rest_framework.views import APIView
from django.contrib.auth import views as auth_views
from .views import transfer_vocabulary, userWord_list, word_list

urlpatterns = [
    #path('userPage/', userWord_list, name="userWordlist"),
    path('', word_list, name = 'word'),
    #path('Word/', auth_views.LoginView.as_view(template_name='Project/chapter.html'), name="room"),
    path('transfer_vocabulary/', transfer_vocabulary, name='transfer_vocabulary'),
    path('delete_word/<int:vocab_id>/', views.delete_word, name='delete_word'),

]

