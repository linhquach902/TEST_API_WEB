# Generated by Django 2.2.2 on 2021-07-16 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_code'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
