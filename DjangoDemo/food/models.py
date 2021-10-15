from enum import Flag
from django.db import models

# Create your models here.
class Destination(models.Model):
    place= models.CharField(max_length=100)
    price= models.IntegerField()
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    offer= models.BooleanField(default=False)