# Generated by Django 3.1.2 on 2020-10-13 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flower_shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='id_customer',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]