from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
    user_id = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(verbose_name="email", max_length=100, blank=True, null=True, unique=True)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = [user_id]


    def _str_(self):
        return self.user_id
    

    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        db_table = 'users'
