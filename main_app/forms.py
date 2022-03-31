from attr import fields
from django.forms import ModelForm
from .models import Item, Character
from django import forms

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name','image','implicit','explicits','item_type','price','api_id']
        widgets = {
                   'image':forms.HiddenInput(),
                   'implicit':forms.HiddenInput(),
                   'explicits':forms.HiddenInput(),
                   'item_type':forms.HiddenInput(),
                   'price':forms.HiddenInput(),
                   'api_id':forms.HiddenInput(),
                   }
#how do I populate this hidden form in my for each statement

class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['name','ascendancy']
    