from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.templatetags.static import static
import requests
from .models import Character, Item
from main_app.books import books_list
from main_app.classes import class_list
from django.views.generic.edit import CreateView, UpdateView, DeleteView

new_book_list = sorted(books_list, key=lambda k: k['year'])

class CharacterCreate(CreateView):
    model = Character
    fields = '__all__'
    # success_url = "/characters/" 

class CharacterUpdate(UpdateView):
    model = Character
    fields = '__all__'

class CharacterDelete(DeleteView):
    model = Character
    success_url = "/characters/"

# Create your views here.
def home(request):
    return render(request,'items/index.html', {'books': new_book_list})
  
def classes(request):
  return render(request,'items/classes.html', {'classes': class_list})

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
  for weapon in weapon_list:
    explicit_holder = ['<p>',]
    for explicit in weapon['explicitModifiers']:
        if explicit['optional'] == True:
          explicit_holder.append('*')
        explicit_holder.append(explicit['text'])
        explicit_holder.append('<br />')
    explicit_holder.pop()
    explicit_holder.append('</p>')
    explicit_split = explicit_holder[0:]
    explicit_string = "\n".join(explicit_split)
    weapon['explicit_holder'] = explicit_string
  return render(request,'items/weapons.html', {'weapon_list': weapon_list})

# def weapons(request):
#   response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=UniqueWeapon')
#   weapons_list = response.json()
#   weapon_list = weapons_list['lines']
#   for weapon in weapon_list:
#     explicit_holder = []
#     for explicit in weapon['explicitModifiers']:
#         explicit = explicit['text']
#     weapon['explicit_holder'] = explicit_holder
#     print(explicit_holder)

def armour(request):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=UniqueArmour')
  armours_list = response.json()
  armour_list = armours_list['lines']
  for armour in armour_list:
    explicit_holder = ['<p>',]
    for explicit in armour['explicitModifiers']:
        if explicit['optional'] == True:
            explicit_holder.append('*')
        explicit_holder.append(explicit['text'])
        explicit_holder.append('<br />')
    explicit_holder.pop()
    explicit_holder.append('</p>')
    explicit_split = explicit_holder[0:]
    explicit_string = "\n".join(explicit_split)
    armour['explicit_holder'] = explicit_string
  return render(request,'items/armour.html', {'armour_list': armour_list})

def accessories(request):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=UniqueAccessory')
  accessories_list = response.json()
  accessory_list = accessories_list['lines']
  for accessory in accessory_list:
    explicit_holder = ['<p>',]
    for explicit in accessory['explicitModifiers']:
        if explicit['optional'] == True:
          explicit_holder.append('*')
        explicit_holder.append(explicit['text'])
        explicit_holder.append('<br />')
    explicit_holder.pop()
    explicit_holder.append('</p>')
    explicit_split = explicit_holder[0:]
    explicit_string = "\n".join(explicit_split)
    accessory['explicit_holder'] = explicit_string
  return render(request,'items/accessories.html', {'accessory_list': accessory_list})

def inventory(request):
    return render(request,'items/inventory.html')
  
def characters(request):
    characters = Character.objects.all()
    return render(request,'items/characters.html', {'characters':characters})
  
def character(request, character_id):
    character = Character.objects.get(id=character_id)
    return render(request,'items/character.html', {'character':character})
  
# class CharacterUpdate(UpdateView):
#   model = Character
#   fields = ['breed','description','age']

def weapon_equip(request):
  print("This is a string - testing")
  print(request.POST)
  item = Item(request.POST)
  print(f"this is the data we are looking for!!! {item}")
  Item.objects.create(name=request.POST.get('name'),image=request.POST.get('image'),implicit=request.POST.get('implicit'),explicits=request.POST.get('explicits'),item_type=request.POST.get('item_type'),price=request.POST.get('price'),api_id=request.POST.get('api_id') )
  # item_insert = item.save(commit=False)
  # item.save()
  return redirect('weapons')
