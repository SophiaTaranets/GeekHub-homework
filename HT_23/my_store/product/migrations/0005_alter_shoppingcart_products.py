# Generated by Django 5.0 on 2024-02-10 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_shoppingcart_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='products',
            field=models.ManyToManyField(related_name='products', to='product.product'),
        ),
    ]
