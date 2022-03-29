from django.urls import path
from . import views
from .models import Character, Item

urlpatterns = [
    path('', views.home, name="home"), #in views folder use home view
    path('items/', views.items, name="index"),
    path('currency/', views.currency, name="currency"),
    path('scarabs/', views.scarabs, name="scarabs"),
    path('weapons/', views.weapons, name="weapons"),
    path('armour/', views.armour, name="armour"),
    path('accessories/', views.accessories, name="accessories"),
    path('inventory/', views.inventory, name="inventory"),
    path('classes/', views.classes, name='classes'),
    path('characters/', views.characters, name='characters'),
    path('character/<int:character_id>', views.character, name="character"),
    path('character/create', views.CharacterCreate.as_view(), name="character_create"),
    path('character/<int:pk>/update/', views.CharacterUpdate.as_view(), name="character_update"),
    path('character/<int:pk>/delete/', views.CharacterDelete.as_view(), name="character_delete"),
    path('weapon_equip/', views.weapon_equip, name="equip_weapon"),
    
]