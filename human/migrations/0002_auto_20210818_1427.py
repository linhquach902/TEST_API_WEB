# Generated by Django 3.2.5 on 2021-08-18 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('human', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='human',
            name='benh_nen',
        ),
        migrations.RemoveField(
            model_name='human',
            name='di_ung',
        ),
        migrations.RemoveField(
            model_name='human',
            name='tien_su_benh',
        ),
    ]
