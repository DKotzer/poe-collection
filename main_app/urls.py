from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), #in views folder use home view
    path('items/', views.items, name="index"),
    path('currency/', views.currency, name="currency"),
    path('scarabs/', views.scarabs, name="scarabs"),
    path('weapons/', views.weapons, name="weapons"),
    path('armour/', views.armour, name="armour"),
    path('accessories/', views.accessories, name="accessories"),
    path('inventory/', views.inventory, name="inventory")
]