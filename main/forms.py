from django.forms import ModelForm
from .models import Item
from django import forms
from django.contrib.auth.models import User

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "price", "description", "user"]
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)