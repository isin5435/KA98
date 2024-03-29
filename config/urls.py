"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import Main, Chapter, Word, login_required_or_redirect_home
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views
from wordData.views import word_list
from wordData.views import userWord_list
from django.conf import settings
from search.views import search_word
from .views import exam
from exam.views import exam, randon_word, test_word
#from .views import Userpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='Project/index.html'), name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', include('user.urls')),
    path('chapter/', auth_views.LoginView.as_view(template_name='Project/chapter.html'),name='chapter'),
    path('Word/', include('wordData.urls') ,name='question_list'),
    path('crawl/', include('crawl.urls')),
    path('search_word', search_word, name='search_word'),
    path('userPage/', login_required_or_redirect_home(userWord_list), name = 'userPage'),
    path('exam/', exam, name='exam'),
    path('random_word/', randon_word, name='random_word'),
    path('test_word/<int:word_id>/', test_word, name='test_word'),
    path('game/',include('game.urls')),

]
