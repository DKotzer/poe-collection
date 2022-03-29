from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=255)
    ascendancy = models.CharField(max_length=255)
    right_hand = models.CharField(max_length=255)
    left_hand = models.CharField(max_length=255)
    helm = models.CharField(max_length=255)
    chest = models.CharField(max_length=255)
    gloves = models.CharField(max_length=255)
    boots = models.CharField(max_length=255)
    belt = models.CharField(max_length=255)
    amulet = models.CharField(max_length=255)
    ring1 = models.CharField(max_length=255)
    ring2 = models.CharField(max_length=255)
    


class Item(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=1000)
    implicit = models.CharField(max_length=255)
    explicits = models.TextField(max_length=2000)
    item_type = models.CharField(max_length=100)
    price = models.IntegerField()
    

