from .models import Dessert         # for us to work with the Dessert Model
from django import forms            # for us to work with Django forms
from django.forms import ModelForm  # for us to use Django ModelForm

# This creates a new form
class dessertForm(forms.ModelForm):

    class Meta:
        model = Dessert
        fields = ('name', 'description', 'price') # must match what I have in the Dessert Model in order for it to work with my database
   