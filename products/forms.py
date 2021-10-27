from django import forms
from .models import Product

class Productform(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'price', 'quantity')