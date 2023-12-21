from django.urls import path
from . import views
from .views import printword

urlpatterns = [
    path('make/', view=views.wordcrawl, name='wordcrawl'),
    path('print/', view=views.printword, name='print'),
    path('makedb/', view=views.makewordbook, name='makewordbook'),
    path('comp/', view=views.comp, name='comp')
]