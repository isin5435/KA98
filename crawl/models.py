from django.db import models

# Create your models here.

class Words(models.Model):
    text =models.CharField(max_length=200)
    definitions = models.CharField(max_length=200, null=True, blank=True)

