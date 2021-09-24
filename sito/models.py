from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    pass


class Compiti(models.Model):
    title = models.CharField(max_length=128)
    img = models.ImageField(upload_to="img/", blank=True)
    code = models.TextField()
    Link = models.URLField(max_length=7000)
