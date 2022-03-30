from django.db import models
from django.urls import reverse
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
    
    def get_absolute_url(self):
        return reverse("character", kwargs={"character_id": self.id})
    
    
    


class Item(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=1000)
    implicit = models.CharField(max_length=400,default=None, blank=True, null=True)
    explicits = models.TextField(max_length=2000,default=None, blank=True, null=True)
    item_type = models.CharField(max_length=100)
    price = models.FloatField()
    api_id = models.IntegerField(default=1)
    #change the on_delete after switching to many to many
    
    

class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=1000)
    item_type = models.CharField(max_length=1000)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    