from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import Product, ShoppingCart, ShoppingCartItem

admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartItem)

