from django.urls import path
from . import views
from .models import Character, Item

urlpatterns = [
    path('', views.home, name="home"), #in views folder use home view
    # path('items/', views.items, name="index"),
    path('currency/', views.currency, name="currency"),
    path('scarabs/', views.scarabs, name="scarabs"),
    path('weapons/', views.weapons, name="weapons"),
    path('armour/', views.armour, name="armour"),
    path('accessories/', views.accessories, name="accessories"),
    path('inventory/', views.inventory, name="inventory"),
    path('classes/', views.classes, name='classes'),
    path('characters/', views.characters, name='characters'),
    path('mycharacters/', views.mycharacters, name='my_characters'),
    path('character/<int:character_id>', views.character, name="character"),
    path('character/create', views.CharacterCreate.as_view(), name="character_create"),
    path('character/<int:pk>/update/', views.CharacterUpdate.as_view(), name="character_update"),
    path('character/<int:pk>/delete/', views.CharacterDelete.as_view(), name="character_delete"),
    path('character/<int:character_id>/add_item', views.add_item, name='add_item'),
    # path('weapon_equip/', views.weapon_equip, name="equip_weapon"),
    # path('armour_equip/', views.armour_equip, name="armour_weapon"),
    # path('accessory_equip/', views.accessory_equip, name="accessory_weapon"),
    
    path('rings/<int:character_id>/', views.rings, name="ring_select"),
    path('rings/<int:character_id>/<int:item_id>', views.ring_equip, name="ring_equip"),
    path('left_rings/<int:character_id>/', views.left_rings, name="left_ring_select"),
    path('left_rings/<int:character_id>/<int:item_id>', views.left_ring_equip, name="left_ring_equip"),
    path('amulets/<int:character_id>/', views.amulets, name="amulet_select"),
    path('amulets/<int:character_id>/<int:item_id>', views.amulet_equip, name="amulet_equip"),
    path('right_weapons/<int:character_id>/', views.right_weapons, name="right_weapon_select"),
    path('right_weapons/<int:character_id>/<int:item_id>', views.right_weapon_equip, name="right_weapon_equip"),
    path('boots/<int:character_id>/', views.boots, name="boots_select"),
    path('boots/<int:character_id>/<int:item_id>', views.boot_equip, name="boot_equip"),
    path('helms/<int:character_id>/', views.helms, name="helm_select"),
    path('helms/<int:character_id>/<int:item_id>', views.helm_equip, name="helm_equip"),
    path('chests/<int:character_id>/', views.chests, name="chest_select"),
    path('chests/<int:character_id>/<int:item_id>', views.chest_equip, name="chest_equip"),
    path('gloves/<int:character_id>/', views.gloves, name="glove_select"),
    path('gloves/<int:character_id>/<int:item_id>', views.glove_equip, name="glove_equip"),
    path('left_weapons/<int:character_id>/', views.left_weapons, name="left_weapon_select"),
    path('left_weapons/<int:character_id>/<int:item_id>', views.left_weapon_equip, name="left_weapon_equip"),
    path('belts/<int:character_id>/', views.belts, name="belt_select"),
    path('belts/<int:character_id>/<int:item_id>', views.belt_equip, name="belt_equip"),
    
    path('accounts/signup',views.signup,name='signup'),
    
    
    # path('characters/<int:character_id>/assos_item/<int:item_id>/', views.assoc_item, name="assoc_item"),
    # path('characters/<int:character_id>/unassos_item/<int:item_id>/', views.unassoc_item, name="unassoc_item"),
    
    
    
]