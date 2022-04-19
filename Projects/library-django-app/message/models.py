from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
