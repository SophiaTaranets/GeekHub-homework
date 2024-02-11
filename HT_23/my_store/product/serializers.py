import sys
from rest_framework import serializers
import subprocess
from .models import Product, ShoppingCart, ProductCategory, ScrapingTask, ShoppingCartItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'product_id', 'category', 'brand_name', 'name', 'price', 'product_url',)


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('name',)


class ShoppingCartSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = ShoppingCart
        fields = ('products', 'user')


class ShoppingCartListSerializer(ShoppingCartSerializer):
    products = ProductSerializer(many=True, read_only=True)


class ShoppingCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = ('product', 'amount', 'shopping_cart')

