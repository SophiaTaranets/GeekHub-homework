from rest_framework import serializers

from .models import Product, ScrapingTask, ShoppingCartItem, ShoppingCart, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:

        model = Product
        fields = ('id', 'product_id', 'category', 'brand_name', 'name', 'price', 'product_url',)


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('name',)


class ScrapingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapingTask
        fields = ('ids',)


class ShoppingCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = ('shopping_cart', 'product', 'amount',)


class ShoppingCartSerializer(serializers.ModelSerializer):
    items = ShoppingCartItemSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ('products',)
