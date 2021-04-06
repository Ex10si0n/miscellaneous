from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

# Create your models here.
class CustomUser(AbstractUser):
    DOB = models.DateField(default=datetime.date(1990, 1, 1))
