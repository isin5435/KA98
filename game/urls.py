from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path("", game.as_view(), name="game"),
    path("get-definitions/", views.get_definitions, name='get-definitions')
]