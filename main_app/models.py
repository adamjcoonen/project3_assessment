from django.db import models
from django.urls import reverse

# Create your models here.

class Widget(models.Model):
    Description = models.CharField(max_length=100)
    
