# Generated by Django 5.0 on 2024-01-02 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_scrapingtask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.TextField(),
        ),
    ]