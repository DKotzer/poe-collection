from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.templatetags.static import static
import requests
from .models import Character, Item
from main_app.books import books_list
from main_app.classes import class_list
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ItemForm
from django.forms import Select


new_book_list = sorted(books_list, key=lambda k: k['year'])

class CharacterCreate(CreateView):
    model = Character
    fields = ['name', 'ascendancy']
    widgets = {
      'ascendancy': Select(attrs={'style': 'width: 400px;'})
    }
    success_url = "/characters/" 

# class CharacterForm(CreateView):
#     model = Character
#     fields = ['name', 'ascendancy']
#     widgets = {
#       'ascendancy': Select(attrs={'style': 'width: 400px;'})
#     }


class CharacterUpdate(UpdateView):
    model = Character
    fields = '__all__'

class CharacterDelete(DeleteView):
    model = Character
    success_url = "/characters/"

# Create your views here.
def home(request):
  characters = Character.objects.all()
  return render(request,'items/characters.html', {'books': new_book_list, 'characters': characters} )
  
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
    item_form = ItemForm()
    item_list = character.items.all()
    return render(request,'items/character.html', {'character':character,'item_form':item_form,'item_list':item_list })
  
# class CharacterUpdate(UpdateView):
#   model = Character
#   fields = ['breed','description','age']


def add_item(request, character_id):
    form = ItemForm(request.POST)
    if form.is_valid():
        new_item = form.save(commit=False)
        new_item.character_id = character_id
        new_item.save()
    return redirect('character', character_id = character_id)
  
def weapon_equip(request):
  print("This is a string - testing below")
  print(request.POST)
  item = Item(request.POST)
  print(f"this is the data we are looking for!!! {item}")
  Item.objects.create(name=request.POST.get('name'),image=request.POST.get('image'),implicit=request.POST.get('implicit'),explicits=request.POST.get('explicits'),item_type=request.POST.get('item_type'),price=request.POST.get('price'),api_id=request.POST.get('api_id') )
  # item_insert = item.save(commit=False)
  # item.save()
  return redirect('weapons')

def armour_equip(request):
  print("This is a string - testing below")
  print(request.POST)
  item = Item(request.POST)
  print(f"this is the data we are looking for!!! {item}")
  Item.objects.create(name=request.POST.get('name'),image=request.POST.get('image'),implicit=request.POST.get('implicit'),explicits=request.POST.get('explicits'),item_type=request.POST.get('item_type'),price=request.POST.get('price'),api_id=request.POST.get('api_id') )
  # item_insert = item.save(commit=False)
  # item.save()
  return redirect('armour')

def accessory_equip(request):
  print("This is a string - testing below")
  print(request.POST)
  item = Item(request.POST)
  print(f"this is the data we are looking for!!! {item}")
  Item.objects.create(name=request.POST.get('name'),image=request.POST.get('image'),implicit=request.POST.get('implicit'),explicits=request.POST.get('explicits'),item_type=request.POST.get('item_type'),price=request.POST.get('price'),api_id=request.POST.get('api_id') )
  # item_insert = item.save(commit=False)
  # item.save()
  return redirect('accessories')




# many to many stuff

def rings(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=UniqueAccessory')
  accessories_list = response.json()
  accessory_list = accessories_list['lines']
  # print(f"this is the accessory list! {ring_list}")
  ring_list = [accessory for accessory in accessory_list if accessory['itemType']=="Ring"]
  for accessory in ring_list:
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
  return render(request,'items/rings.html', {'ring_list': ring_list, 'character_id':character_id})

def ring_equip(request, character_id, item_id):
  
  item = Item.objects.create(
    name=request.POST['name'],
    image=request.POST['image'],
    implicit=request.POST['implicit'],
    explicits=request.POST['explicits'],
    item_type=request.POST['item_type'],
    price=request.POST['price'],
    api_id = request.POST['api_id'],
  )
  Character.objects.get(id=character_id).items.add(item)
  char = Character.objects.get(pk=character_id)
  char.ring2 = image=request.POST['image']
  char.save() 
  #
  return redirect('character', character_id=character_id)


def left_rings(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=UniqueAccessory')
  accessories_list = response.json()
  accessory_list = accessories_list['lines']
  # print(f"this is the accessory list! {left_ring_list}")
  left_ring_list = [accessory for accessory in accessory_list if accessory['itemType']=="Ring"]
  for accessory in left_ring_list:
    explicit_holder = ['<p>',]
    for explicit in accessory['explicitModifiers']:
        if explicit['optional'] == True:
          explicit_holder.append('*')
        explicit_holder.append(explicit['text'])
        explicit_holder.append('<br />')
    explicit_holder.pop()
    explicit_holder.append('</p>')
    explicit_split = explicit_holder[0:]
    explicit_stleft_ring = "\n".join(explicit_split)
    accessory['explicit_holder'] = explicit_stleft_ring
  return render(request,'items/left_rings.html', {'left_ring_list': left_ring_list, 'character_id':character_id})

def left_ring_equip(request, character_id, item_id):
  
  item = Item.objects.create(
    name=request.POST['name'],
    image=request.POST['image'],
    implicit=request.POST['implicit'],
    explicits=request.POST['explicits'],
    item_type=request.POST['item_type'],
    price=request.POST['price'],
    api_id = request.POST['api_id'],
  )
  Character.objects.get(id=character_id).items.add(item)
  char = Character.objects.get(pk=character_id)
  char.ring1 = image=request.POST['image']
  char.save() 
  #
  return redirect('character', character_id=character_id)

def amulets(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=UniqueAccessory')
  accessories_list = response.json()
  accessory_list = accessories_list['lines']
  # print(f"this is the accessory list! {amulet_list}")
  amulet_list = [accessory for accessory in accessory_list if accessory['itemType']=="Amulet"]
  for accessory in amulet_list:
    explicit_holder = ['<p>',]
    for explicit in accessory['explicitModifiers']:
        if explicit['optional'] == True:
          explicit_holder.append('*')
        explicit_holder.append(explicit['text'])
        explicit_holder.append('<br />')
    explicit_holder.pop()
    explicit_holder.append('</p>')
    explicit_split = explicit_holder[0:]
    explicit_stamulet = "\n".join(explicit_split)
    accessory['explicit_holder'] = explicit_stamulet
  
  return render(request,'items/amulets.html', {'amulet_list': amulet_list, 'character_id':character_id})

def amulet_equip(request, character_id, item_id):
  
  item = Item.objects.create(
    name=request.POST['name'],
    image=request.POST['image'],
    implicit=request.POST['implicit'],
    explicits=request.POST['explicits'],
    item_type=request.POST['item_type'],
    price=request.POST['price'],
    api_id = request.POST['api_id'],
  )
  Character.objects.get(pk=character_id).items.add(item)
  char = Character.objects.get(pk=character_id)
  char.amulet = image=request.POST['image']
  char.save() 
  return redirect('character', character_id=character_id)
  

def right_weapons(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=UniqueWeapon')
  weapons_list = response.json()
  weapon_list = weapons_list['lines']
  # print(f"this is the accessory list! {right_weapon_list}")
  right_weapon_list = [weapon for weapon in weapon_list if weapon['flavourText']!=""]
  for accessory in right_weapon_list:
    explicit_holder = ['<p>',]
    for explicit in accessory['explicitModifiers']:
        if explicit['optional'] == True:
          explicit_holder.append('*')
        explicit_holder.append(explicit['text'])
        explicit_holder.append('<br />')
    explicit_holder.pop()
    explicit_holder.append('</p>')
    explicit_split = explicit_holder[0:]
    explicit_stright_weapon = "\n".join(explicit_split)
    accessory['explicit_holder'] = explicit_stright_weapon
  return render(request,'items/right_weapons.html', {'right_weapon_list': right_weapon_list, 'character_id':character_id})

def right_weapon_equip(request, character_id, item_id):
  char = Character.objects.get(pk=character_id)
  if char.right_hand != "/static/imgs/plus.png":
    print("testtesttest")
    # weapon_select = char.filter(item_type)
    oldleft_weapon = Item.objects.filter(character=character_id, item_type__in = ['One Handed Sword', 'Two Handed Sword', 'Staff', 'Two Handed Axe', 'One Handed Axe', 'Two Handed Mace', 'Bow', 'One Handed Mace', 'Dagger', 'Wand', 'Claw'])
    print("old weapon", oldleft_weapon)
    # oldleft_weapon = Item.objects.get(character=character_id , and item_type in ['One' 'Handed Sword', 'Two Handed' 'Sword', 'Staff'])
    # oldleft_weapon = Item.objects.get(character=character_id , and item_type in ['One' 'Handed Sword', 'Two Handed' 'Sword', 'Staff'])
    
    # One Handed Sword, Two Handed Sword, Staff, Two Handed Axe, One Handed Axe, Two Handed Mace, Bow, One Handed Mace, Dagger, Wand, Claw
    # print(oldleft_weapon.id)
    oldleft_weapon.delete()
  
  item = Item.objects.create(
    name=request.POST['name'],
    image=request.POST['image'],
    implicit=request.POST['implicit'],
    explicits=request.POST['explicits'],
    item_type=request.POST['item_type'],
    price=request.POST['price'],
    api_id = request.POST['api_id'],
  )
  Character.objects.get(id=character_id).items.add(item)
  char = Character.objects.get(pk=character_id)
  char.right_hand = image=request.POST['image']
  char.save() 
  return redirect('character', character_id=character_id)



def boots(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=UniqueArmour')
  armours_list = response.json()
  armour_list = armours_list['lines']
  
  
  boot_list = [armour for armour in armour_list if armour['itemType']=="Boots"]
  for armour in boot_list:
    explicit_holder = ['<p>',]
    for explicit in armour['explicitModifiers']:
        if explicit['optional'] == True:
          explicit_holder.append('*')
        explicit_holder.append(explicit['text'])
        explicit_holder.append('<br />')
    explicit_holder.pop()
    explicit_holder.append('</p>')
    explicit_split = explicit_holder[0:]
    explicit_stboot = "\n".join(explicit_split)
    armour['explicit_holder'] = explicit_stboot
  return render(request,'items/boots.html', {'boot_list': boot_list, 'character_id':character_id})

def boot_equip(request, character_id, item_id):
  
  item = Item.objects.create(
    name=request.POST['name'],
    image=request.POST['image'],
    implicit=request.POST['implicit'],
    explicits=request.POST['explicits'],
    item_type=request.POST['item_type'],
    price=request.POST['price'],
    api_id = request.POST['api_id'],
  )
  Character.objects.get(id=character_id).items.add(item)
  char = Character.objects.get(pk=character_id)
  char.boots = image=request.POST['image']
  char.save() 
  #
  return redirect('character', character_id=character_id)

def helms(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=UniqueArmour')
  armours_list = response.json()
  armour_list = armours_list['lines']
  
  
  helm_list = [armour for armour in armour_list if armour['itemType']=="Helmet"]
  for armour in helm_list:
    explicit_holder = ['<p>',]
    for explicit in armour['explicitModifiers']:
        if explicit['optional'] == True:
          explicit_holder.append('*')
        explicit_holder.append(explicit['text'])
        explicit_holder.append('<br />')
    explicit_holder.pop()
    explicit_holder.append('</p>')
    explicit_split = explicit_holder[0:]
    explicit_sthelm = "\n".join(explicit_split)
    armour['explicit_holder'] = explicit_sthelm
  return render(request,'items/helms.html', {'helm_list': helm_list, 'character_id':character_id})

def helm_equip(request, character_id, item_id):
  
  item = Item.objects.create(
    name=request.POST['name'],
    image=request.POST['image'],
    implicit=request.POST['implicit'],
    explicits=request.POST['explicits'],
    item_type=request.POST['item_type'],
    price=request.POST['price'],
    api_id = request.POST['api_id'],
  )
  Character.objects.get(id=character_id).items.add(item)
  char = Character.objects.get(pk=character_id)
  char.helm = image=request.POST['image']
  char.save() 
  #
  return redirect('character', character_id=character_id)

def chests(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=UniqueArmour')
  armours_list = response.json()
  armour_list = armours_list['lines']
  chest_list = [armour for armour in armour_list if armour['itemType']=="Body Armour"]
  for armour in chest_list:
    explicit_holder = ['<p>',]
    for explicit in armour['explicitModifiers']:
        if explicit['optional'] == True:
          explicit_holder.append('*')
        explicit_holder.append(explicit['text'])
        explicit_holder.append('<br />')
    explicit_holder.pop()
    explicit_holder.append('</p>')
    explicit_split = explicit_holder[0:]
    explicit_stchest = "\n".join(explicit_split)
    armour['explicit_holder'] = explicit_stchest
  return render(request,'items/chests.html', {'chest_list': chest_list, 'character_id':character_id})

def chest_equip(request, character_id, item_id):
  
  item = Item.objects.create(
    name=request.POST['name'],
    image=request.POST['image'],
    implicit=request.POST['implicit'],
    explicits=request.POST['explicits'],
    item_type=request.POST['item_type'],
    price=request.POST['price'],
    api_id = request.POST['api_id'],
  )
  Character.objects.get(id=character_id).items.add(item)
  char = Character.objects.get(pk=character_id)
  char.chest = image=request.POST['image']
  char.save() 
  #
  return redirect('character', character_id=character_id)

def gloves(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=UniqueArmour')
  armours_list = response.json()
  armour_list = armours_list['lines']
  glove_list = [armour for armour in armour_list if armour['itemType']=="Gloves"]
  for armour in glove_list:
    explicit_holder = ['<p>',]
    for explicit in armour['explicitModifiers']:
        if explicit['optional'] == True:
          explicit_holder.append('*')
        explicit_holder.append(explicit['text'])
        explicit_holder.append('<br />')
    explicit_holder.pop()
    explicit_holder.append('</p>')
    explicit_split = explicit_holder[0:]
    explicit_stglove = "\n".join(explicit_split)
    armour['explicit_holder'] = explicit_stglove
    
    
  return render(request,'items/gloves.html', {'glove_list': glove_list, 'character_id':character_id})

def glove_equip(request, character_id, item_id):
  
  char = Character.objects.get(pk=character_id)
  if char.gloves != "/static/imgs/plus.png":
    oldglove = Item.objects.get(character=character_id , item_type = 'Gloves')
    
    oldglove.delete()
  
  item = Item.objects.create(
    name=request.POST['name'],
    image=request.POST['image'],
    implicit=request.POST['implicit'],
    explicits=request.POST['explicits'],
    item_type=request.POST['item_type'],
    price=request.POST['price'],
    api_id = request.POST['api_id'],
  )
  Character.objects.get(id=character_id).items.add(item)
  char = Character.objects.get(pk=character_id)
  char.gloves = image=request.POST['image']
  char.save() 
  #
  return redirect('character', character_id=character_id)


def left_weapons(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=UniqueArmour')
  armours_list = response.json()
  armour_list = armours_list['lines']
  left_weapon_list = [armour for armour in armour_list if armour['itemType']=="Quiver" or armour['itemType']=="Shield"]
  for armour in left_weapon_list:
    explicit_holder = ['<p>',]
    for explicit in armour['explicitModifiers']:
        if explicit['optional'] == True:
          explicit_holder.append('*')
        explicit_holder.append(explicit['text'])
        explicit_holder.append('<br />')
    explicit_holder.pop()
    explicit_holder.append('</p>')
    explicit_split = explicit_holder[0:]
    explicit_stleft_weapon = "\n".join(explicit_split)
    armour['explicit_holder'] = explicit_stleft_weapon
  return render(request,'items/left_weapons.html', {'left_weapon_list': left_weapon_list, 'character_id':character_id})

def left_weapon_equip(request, character_id, item_id):
  
  
  item = Item.objects.create(
    name=request.POST['name'],
    image=request.POST['image'],
    implicit=request.POST['implicit'],
    explicits=request.POST['explicits'],
    item_type=request.POST['item_type'],
    price=request.POST['price'],
    api_id = request.POST['api_id'],
  )
  Character.objects.get(id=character_id).items.add(item)
  char = Character.objects.get(pk=character_id)
  char.left_hand = image=request.POST['image']
  char.save() 
  #
  return redirect('character', character_id=character_id)

def belts(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=UniqueAccessory')
  accessories_list = response.json()
  accessory_list = accessories_list['lines']
  # print(f"this is the accessory list! {amulet_list}")
  belt_list = [accessory for accessory in accessory_list if accessory['itemType']=="Belt"]
  for armour in belt_list:
    explicit_holder = ['<p>',]
    for explicit in armour['explicitModifiers']:
        if explicit['optional'] == True:
          explicit_holder.append('*')
        explicit_holder.append(explicit['text'])
        explicit_holder.append('<br />')
    explicit_holder.pop()
    explicit_holder.append('</p>')
    explicit_split = explicit_holder[0:]
    explicit_stbelt = "\n".join(explicit_split)
    armour['explicit_holder'] = explicit_stbelt
  return render(request,'items/belts.html', {'belt_list': belt_list, 'character_id':character_id})

def belt_equip(request, character_id, item_id):
  #if belt image is not default, find belt in items that matches character_id and delete it
  char = Character.objects.get(pk=character_id)
  if char.belt != "/static/imgs/smallplus.png":
    oldbelt = Item.objects.get(character=character_id , item_type = 'Belt')
    print(oldbelt.id)
    oldbelt.delete()
  
  item = Item.objects.create(
    name=request.POST['name'],
    image=request.POST['image'],
    implicit=request.POST['implicit'],
    explicits=request.POST['explicits'],
    item_type=request.POST['item_type'],
    price=request.POST['price'],
    api_id = request.POST['api_id'],
  )
  Character.objects.get(id=character_id).items.add(item)
  char.belt = image=request.POST['image']
  char.save() 
  #
  return redirect('character', character_id=character_id)