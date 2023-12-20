from django.db import models
from django.contrib.auth.models import User

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

class UserVocabulary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vocabulary = models.ForeignKey(Word, on_delete=models.CASCADE)
    added_date= models.DateTimeField(auto_now=True)
    def __int__(self):
        return self.int
