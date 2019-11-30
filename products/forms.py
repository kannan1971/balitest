from django import forms
from .models import Product

# Method 1
class Product_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
              'title',
              'description',
              'price'
        ]

# Method 2 -Raw DJANGO form

class product_raw_form(forms.Form):
    title       = forms.CharField()
    description = forms.CharField()
    price       = forms.DecimalField()
