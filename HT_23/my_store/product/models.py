from django.contrib.auth.models import User
from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.TextField(blank=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=70, default='Product brand')
    name = models.CharField(max_length=500, default='Product title')
    price = models.DecimalField(max_digits=10, decimal_places=2, default='0,00')
    product_url = models.TextField(max_length=100, default='Default url')


class ScrapingTask(models.Model):
    ids = models.TextField(max_length=2000, default='Enter ids')

    def __str__(self):
        return self.ids


class ShoppingCart(models.Model):
    products = models.ManyToManyField(Product, related_name='products')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)


class ShoppingCartItem(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(f'{self.amount} x {self.product}')


