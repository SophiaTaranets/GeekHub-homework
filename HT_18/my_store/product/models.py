from django.db import models


class Product(models.Model):
    product_id = models.TextField(blank=False)
    category = models.TextField(max_length=70, default='Product category')
    brand_name = models.CharField(max_length=70, default='Product brand')
    name = models.CharField(max_length=500, default='Product title')
    price = models.DecimalField(max_digits=10, decimal_places=2, default='0,00')
    product_url = models.TextField(max_length=100, default='Default url')


class ScrapingTask(models.Model):
    ids = models.TextField(max_length=2000, default='Enter ids')

    def __str__(self):
        return self.ids
