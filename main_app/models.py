
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

ASCENDS= (
    ('https://poe.ninja/images/classes/Slayer_avatar.png','Slayer'),
    ('https://poe.ninja/images/classes/Gladiator_avatar.png','Gladiator'),
    ('https://poe.ninja/images/classes/Champion_avatar.png', 'Champion'),
    ('https://poe.ninja/images/classes/Assassin_avatar.png', 'Assassin '),
    ('https://poe.ninja/images/classes/Saboteur_avatar.png', 'Saboteur '),
    ('https://poe.ninja/images/classes/Trickster_avatar.png', 'Trickster'),
    ('https://poe.ninja/images/classes/Juggernaut_avatar.png', 'Juggernaut '),
    ('https://poe.ninja/images/classes/Berserker_avatar.png', 'Berserker '),
    ('https://poe.ninja/images/classes/Chieftain_avatar.png', 'Chieftain '),
    ('https://poe.ninja/images/classes/Necromancer_avatar.png', 'Necromancer'),
    ('https://poe.ninja/images/classes/Elementalist_avatar.png', 'Elementalist'),
    ('https://poe.ninja/images/classes/Occultist_avatar.png', 'Occultist'),
    ('https://poe.ninja/images/classes/Deadeye_avatar.png', 'Deadeye'),
    ('https://poe.ninja/images/classes/Raider_avatar.png', 'Raider'),
    ('https://poe.ninja/images/classes/Pathfinder_avatar.png', 'Pathfinder'),
    ('https://poe.ninja/images/classes/Inquisitor_avatar.png', 'Inquisitor'),
    ('https://poe.ninja/images/classes/Hierophant_avatar.png', 'Hierophant'),
    ('https://poe.ninja/images/classes/Guardian_avatar.png', 'Guardian'),
    ('https://poe.ninja/images/classes/Ascendant_avatar.png', 'Ascendant'),
)

     
class Item(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=1000)
    implicit = models.CharField(max_length=400,default=None, blank=True, null=True)
    explicits = models.TextField(max_length=2000,default=None, blank=True, null=True)
    item_type = models.CharField(max_length=100)
    price = models.FloatField()
    api_id = models.IntegerField(default=1)
    item_slot = models.CharField(max_length=1000, default=None, blank=True, null=True)
    # character = models.ForeignKey(Character, on_delete=models.CASCADE, default=1)
    #change the on_delete after switching to many to many
    def __str__(self):
        return f"{self.name} ({self.item_type})"
    class Meta:
        ordering = ['-price']

    

class Character(models.Model):
    name = models.CharField(max_length=255)
    ascendancy = models.CharField(max_length=100, choices=ASCENDS, default='Slayer')
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse("character", kwargs={"character_id": self.id})
    
    def __str__(self):
        return self.name




