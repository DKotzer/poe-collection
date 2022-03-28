from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=1000)
    implicit = models.CharField(max_length=255)
    explicits = models.TextField(max_length=2000)
    price = models.IntegerField()
    

