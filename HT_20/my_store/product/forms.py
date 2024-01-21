from django import forms
from django.core.validators import MinValueValidator
from django.forms import ModelForm, Textarea
from .models import ScrapingTask, Product


class IDForm(ModelForm):
   class Meta:
      model = ScrapingTask
      fields = ('ids',)
      widgets = {'ids': Textarea(attrs={'cols': 20, 'rows': 10})}


class ProductForm(forms.ModelForm):
   class Meta:
      model = Product
      fields = ['category', 'brand_name', 'name', 'price', 'product_url']
   price = forms.DecimalField(
      validators=[MinValueValidator(1)],
      widget=forms.NumberInput(attrs={'min': '1'})
   )
