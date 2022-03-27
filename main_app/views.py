from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
import requests
from main_app.books import books_list


new_book_list = sorted(books_list, key=lambda k: k['year'])

# Create your views here.
def home(request):
    return render(request,'items/index.html', {'books': new_book_list})

def about(request):
    return render(request,'about.html')

def items(request):
    return render(request,'items/index.html', {'books': new_book_list})

def currency(request):
  response = requests.get('https://poe.ninja/api/data/currencyoverview?league=Archnemesis&type=Currency')
  currencies_list = response.json()
  currencies_list2 = currencies_list['currencyDetails']
  return render (request,'items/currency.html', {'currency_list': currencies_list2} )
# def currency(request):
#     return render(request,'items/currency.html', {'currency_list': currencyDetails})
  
def scarabs(request):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=Scarab')
  scarabs_list = response.json()
  scarab_list = scarabs_list['lines']
  return render(request,'items/scarabs.html', {'scarab_list': scarab_list})
  
def weapons(request):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=UniqueWeapon')
  weapons_list = response.json()
  weapon_list = weapons_list['lines']
  return render(request,'items/weapons.html', {'weapon_list': weapon_list})

def armour(request):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=UniqueArmour')
  armours_list = response.json()
  armour_list = armours_list['lines']
  return render(request,'items/armour.html', {'armour_list': armour_list})

def accessories(request):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=UniqueAccessory')
  accessories_list = response.json()
  accessory_list = accessories_list['lines']
  return render(request,'items/accessories.html', {'accessory_list': accessory_list})

