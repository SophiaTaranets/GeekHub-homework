import sys
from rest_framework import serializers
import subprocess

from .models import Product, ShoppingCart, ProductCategory, ScrapingTask, ShoppingCartItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',
                 'product_id',
                  'category',
                  'brand_name',
                  'name',
                  'price',
                  'product_url',)


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('name',)


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = ('product', 'amount',)


class ShoppingCartListSerializer(ShoppingCartSerializer):
    class Meta:
        model = ShoppingCart
        fields = ('products',)
    products = ProductSerializer(many=True, read_only=True)


class ShoppingCartCreateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()

    @staticmethod
    def get_product_id(value):
        try:
            Product.objects.get(pk=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError('No product with this id')
        return value


class ShoppingCartUpdateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    @staticmethod
    def get_product_id(value):
        try:
            Product.objects.get(pk=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError('No product with this id')
        return value


class ShoppingCartDeleteSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required=False)

    @staticmethod
    def get_product_id(value):
        try:
            Product.objects.get(pk=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product with this id does not exist.")
        return value


class ScrapingTaskSerializer(serializers.Serializer):
    class Meta:
        model = ScrapingTask
        fields = ('ids',)

    def run_scraping_subprocess(self, products_array):
        sub_process = subprocess.Popen([
            sys.executable,
            'manage.py',
            'run_scraping',
            products_array['products_array']
        ])
        print(f'{sub_process.pid}')
        return products_array
