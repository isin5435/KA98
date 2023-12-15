from django.contrib import admin

# Register your models here.
from .models import Word,DestinationVocabulary


admin.site.register(Word)
admin.site.register(DestinationVocabulary)