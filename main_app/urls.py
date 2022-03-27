from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), #in views folder use home view
    path('about/', views.about, name="about"),
    path('items/', views.items, name="index"),
    path('currency/', views.currency, name="currency"),
    path('scarabs/', views.scarabs, name="scarabs"),
    path('weapons/', views.weapons, name="weapons")
]