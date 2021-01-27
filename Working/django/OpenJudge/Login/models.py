from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    comment = models.CharField(max_length=500)
    email = models.CharField(max_length=50)
    school = models.CharField(max_length=100)
