
from django.db import models
from django.urls import reverse

# Create your models here.
     
class Item(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=1000)
    implicit = models.CharField(max_length=400,default=None, blank=True, null=True)
    explicits = models.TextField(max_length=2000,default=None, blank=True, null=True)
    item_type = models.CharField(max_length=100)
    price = models.FloatField()
    api_id = models.IntegerField(default=1)
    # item_slot = models.CharField(max_length=100, default=None, blank=True, null=True)
    # character = models.ForeignKey(Character, on_delete=models.CASCADE, default=1)
    #change the on_delete after switching to many to many
    def __str__(self):
        return f"{self.name} ({self.item_type})"
    class Meta:
        ordering = ['-price']

    

class Character(models.Model):
    name = models.CharField(max_length=255)
    ascendancy = models.CharField(max_length=255, default=None, blank=True)
    right_hand = models.CharField(max_length=255, default="/static/imgs/plus.png", blank=True)
    left_hand = models.CharField(max_length=255, default="/static/imgs/plus.png", blank=True)
    helm = models.CharField(max_length=255, default="/static/imgs/plus.png", blank=True)
    chest = models.CharField(max_length=255, default="/static/imgs/plus.png", blank=True)
    gloves = models.CharField(max_length=255, default="/static/imgs/plus.png", blank=True)
    boots = models.CharField(max_length=255, default="/static/imgs/plus.png", blank=True)
    belt = models.CharField(max_length=255, default="/static/imgs/smallplus.png", blank=True)
    amulet = models.CharField(max_length=255, default="/static/imgs/smallplus.png", blank=True)
    ring1 = models.CharField(max_length=255, default="/static/imgs/smallplus.png", blank=True)
    ring2 = models.CharField(max_length=255, default="/static/imgs/smallplus.png", blank=True)
    items = models.ManyToManyField(Item)
    
    def get_absolute_url(self):
        return reverse("character", kwargs={"character_id": self.id})
    
    def __str__(self):
        return {self.name}




