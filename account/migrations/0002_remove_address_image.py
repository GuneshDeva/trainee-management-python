# Generated by Django 4.2.2 on 2023-07-15 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='image',
        ),
    ]