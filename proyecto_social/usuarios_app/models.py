from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class Usuario(AbstractUser):
    age = models.IntegerField()
    bio = models.TextField()