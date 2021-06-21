from django.db import models
from django.urls import reverse

# Create your models here.
class post(models.Model):
    title = models.TextField()
    date = models.DateField(auto_now_add=True)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('posts')