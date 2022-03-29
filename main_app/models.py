from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=255)
    ascendancy = models.CharField(max_length=255, default=None, blank=True)
    right_hand = models.CharField(max_length=255, default=None, blank=True)
    left_hand = models.CharField(max_length=255, default=None, blank=True)
    helm = models.CharField(max_length=255, default=None, blank=True)
    chest = models.CharField(max_length=255, default=None, blank=True)
    gloves = models.CharField(max_length=255, default=None, blank=True)
    boots = models.CharField(max_length=255, default=None, blank=True)
    belt = models.CharField(max_length=255, default=None, blank=True)
    amulet = models.CharField(max_length=255, default=None, blank=True)
    ring1 = models.CharField(max_length=255, default=None, blank=True)
    ring2 = models.CharField(max_length=255, default=None, blank=True)
    


class Item(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=1000)
    implicit = models.CharField(max_length=255)
    explicits = models.TextField(max_length=2000)
    item_type = models.CharField(max_length=100)
    price = models.IntegerField()
    

