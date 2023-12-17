from django.db import models

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=100)
    definition = models.TextField()
    example = models.TextField()

   

class DestinationVocabulary(models.Model):
    word = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=100)
    definition = models.TextField()
    example = models.TextField()

