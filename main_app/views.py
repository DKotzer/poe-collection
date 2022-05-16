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
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import os
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

new_book_list = sorted(books_list, key=lambda k: k['year'])

class CharacterCreate(LoginRequiredMixin, CreateView):
    model = Character
    fields = ['name', 'ascendancy']
    widgets = {
      'ascendancy': Select(attrs={'style': 'width: 400px;'})
    }
    
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)
    # success_url = "/mycharacters/" 
# class CharacterForm(CreateView):
#     model = Character
#     fields = ['name', 'ascendancy']
#     widgets = {
#       'ascendancy': Select(attrs={'style': 'width: 400px;'})
#     }


class CharacterUpdate(LoginRequiredMixin, UpdateView):
    model = Character
    fields = '__all__'

class CharacterDelete(LoginRequiredMixin, DeleteView):
    model = Character
    success_url = "/characters/"

# Create your views here.
@login_required
def home(request):
  characters = Character.objects.filter(user=request.user)
    
  return render(request,'items/mycharacters.html', {'characters':characters})
  
def classes(request):
  return render(request,'items/classes.html', {'classes': class_list})

def items(request):
    return render(request,'items/index.html', {'books': new_book_list})

def currency(request):
  response = requests.get('https://poe.ninja/api/data/currencyoverview?league=Sentinel&type=Currency')
  currencies_list = response.json()
  currencies_list2 = currencies_list['currencyDetails'] 
  return render (request,'items/currency.html', {'currency_list': currencies_list2} )
# def currency(request):
#     return render(request,'items/currency.html', {'currency_list': currencyDetails})
  
def scarabs(request):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Sentinel&type=Scarab')
  scarabs_list = response.json()
  scarab_list = scarabs_list['lines']
  return render(request,'items/scarabs.html', {'scarab_list': scarab_list})
  
def weapons(request):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Sentinel&type=UniqueWeapon')
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
    #infiniscroll test
  
  page = request.GET.get('page', 1)
  paginator = Paginator(weapon_list, 60)
  try:
      weapons = paginator.page(page)
  except PageNotAnInteger:
      weapons = paginator.page(1)
  except EmptyPage:
      weapons = paginator.page(paginator.num_pages)
    
  return render(request,'items/weapons.html', {'weapon_list': weapon_list, 'weapons': weapons})

# def weapons(request):
#   response = requests.get('https://poe.ninja/api/data/itemoverview?league=Sentinel&type=UniqueWeapon')
#   weapons_list = response.json()
#   weapon_list = weapons_list['lines']
#   for weapon in weapon_list:
#     explicit_holder = []
#     for explicit in weapon['explicitModifiers']:
#         explicit = explicit['text']
#     weapon['explicit_holder'] = explicit_holder
#     print(explicit_holder)

def armour(request):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Sentinel&type=UniqueArmour')
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
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Sentinel&type=UniqueAccessory')
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
@login_required  
def characters(request):
    characters = Character.objects.all()
    
    return render(request,'items/characters.html', {'characters':characters})
@login_required  
def mycharacters(request):
    characters = Character.objects.filter(user=request.user)
    
    return render(request,'items/mycharacters.html', {'characters':characters})
@login_required  
def character(request, character_id):
    character = Character.objects.get(id=character_id)
    item_form = ItemForm()
    item_list = character.items.all()
    total_value = 0;
    for item in item_list:
      total_value += item.price
    total_value = round(total_value, 1)
    return render(request,'items/character.html', {'character':character,'item_form':item_form,'item_list':item_list, 'total_value':total_value})
  
# class CharacterUpdate(UpdateView):
#   model = Character
#   fields = ['breed','description','age']

@login_required
def add_item(request, character_id):
    form = ItemForm(request.POST)
    if form.is_valid():
        new_item = form.save(commit=False)
        new_item.character_id = character_id
        new_item.save()
    return redirect('character', character_id = character_id)
  
# def weapon_equip(request):
#   print("This is a string - testing below")
#   print(request.POST)
#   item = Item(request.POST)
#   print(f"this is the data we are looking for!!! {item}")
#   Item.objects.create(name=request.POST.get('name'),image=request.POST.get('image'),implicit=request.POST.get('implicit'),explicits=request.POST.get('explicits'),item_type=request.POST.get('item_type'),price=request.POST.get('price'),api_id=request.POST.get('api_id') )
#   # item_insert = item.save(commit=False)
#   # item.save()
#   return redirect('weapons')

# def armour_equip(request):
#   print("This is a string - testing below")
#   print(request.POST)
#   item = Item(request.POST)
#   print(f"this is the data we are looking for!!! {item}")
#   Item.objects.create(name=request.POST.get('name'),image=request.POST.get('image'),implicit=request.POST.get('implicit'),explicits=request.POST.get('explicits'),item_type=request.POST.get('item_type'),price=request.POST.get('price'),api_id=request.POST.get('api_id') )
#   # item_insert = item.save(commit=False)
#   # item.save()
#   return redirect('armour')

# def accessory_equip(request):
#   print("This is a string - testing below")
#   print(request.POST)
#   item = Item(request.POST)
#   print(f"this is the data we are looking for!!! {item}")
#   Item.objects.create(name=request.POST.get('name'),image=request.POST.get('image'),implicit=request.POST.get('implicit'),explicits=request.POST.get('explicits'),item_type=request.POST.get('item_type'),price=request.POST.get('price'),api_id=request.POST.get('api_id') )
#   # item_insert = item.save(commit=False)
#   # item.save()
#   return redirect('accessories')




# many to many stuff
@login_required
def rings(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Sentinel&type=UniqueAccessory')
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
@login_required
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

@login_required
def left_rings(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Sentinel&type=UniqueAccessory')
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
@login_required
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
@login_required
def amulets(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Sentinel&type=UniqueAccessory')
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
@login_required
def amulet_equip(request, character_id, item_id):
  
  char = Character.objects.get(pk=character_id)
  if char.amulet != "/static/imgs/smallplus.png":
    oldamulet = Item.objects.get(character=character_id , item_type = 'Amulet')
    
    oldamulet.delete()
  
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
  
@login_required
def right_weapons(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Sentinel&type=UniqueWeapon')
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
@login_required
def right_weapon_equip(request, character_id, item_id):
  char = Character.objects.get(pk=character_id)
  if char.right_hand != "/static/imgs/plus.png":
    oldright_weapon = Item.objects.filter(character=character_id, item_type__in = ['One Handed Sword', 'Two Handed Sword', 'Staff', 'Two Handed Axe', 'One Handed Axe', 'Two Handed Mace', 'Bow', 'One Handed Mace', 'Dagger', 'Wand', 'Claw'])
    oldright_weapon.delete()
  
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


@login_required
def boots(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Sentinel&type=UniqueArmour')
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
@login_required
def boot_equip(request, character_id, item_id):
  
  char = Character.objects.get(pk=character_id)
  if char.boots != "/static/imgs/plus.png":
    oldboots = Item.objects.get(character=character_id , item_type = 'Boots')
    
    oldboots.delete()
  
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
@login_required
def helms(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Sentinel&type=UniqueArmour')
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
@login_required
def helm_equip(request, character_id, item_id):
  char = Character.objects.get(pk=character_id)
  if char.helm != "/static/imgs/plus.png":
    oldhelm = Item.objects.get(character=character_id , item_type = 'Helmet')
    
    oldhelm.delete()
  
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
@login_required
def chests(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Sentinel&type=UniqueArmour')
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
@login_required
def chest_equip(request, character_id, item_id):
  char = Character.objects.get(pk=character_id)
  if char.chest != "/static/imgs/plus.png":
    oldchest = Item.objects.get(character=character_id , item_type = 'Body Armour')
    
    oldchest.delete()
  
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
@login_required
def gloves(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Sentinel&type=UniqueArmour')
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
@login_required
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

@login_required
def left_weapons(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Sentinel&type=UniqueArmour')
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
@login_required
def left_weapon_equip(request, character_id, item_id):
  
    
  char = Character.objects.get(pk=character_id)
  if char.right_hand != "/static/imgs/plus.png":
    oldleft_weapon = Item.objects.filter(character=character_id, item_type__in = ['Shield', 'Quiver'])
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
  char.left_hand = image=request.POST['image']
  char.save() 
  #
  return redirect('character', character_id=character_id)
@login_required
def belts(request, character_id):
  response = requests.get('https://poe.ninja/api/data/itemoverview?league=Sentinel&type=UniqueAccessory')
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
@login_required
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

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #save user to DB
            user = form.save()
            #login the user
            login(request, user)
            return redirect('index')
        else:
            error_message = "Invalid Sign Up Submission - Try Again"
    form = UserCreationForm()
    context = {'form':form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)