# Generated by Django 3.2.5 on 2021-08-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_vendor_accept_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='accept_card',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
