# Generated by Django 3.2.5 on 2021-08-09 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='tax_ID',
        ),
    ]