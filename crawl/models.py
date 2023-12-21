from django.db import models

# Create your models here.

class Words(models.Model):
    word =models.CharField(max_length=200)
    definition = models.CharField(max_length=200, null=True, blank=True)

