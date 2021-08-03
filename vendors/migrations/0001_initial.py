# Generated by Django 3.2.5 on 2021-08-03 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('vendor_ID', models.CharField(max_length=50)),
                ('tax_ID', models.CharField(max_length=50)),
                ('point_contact_name', models.CharField(max_length=200)),
                ('vendor_address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('vendor_email', models.CharField(max_length=100)),
                ('company_type', models.CharField(max_length=200)),
            ],
        ),
    ]
