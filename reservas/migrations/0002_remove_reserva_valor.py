# Generated by Django 4.2.5 on 2023-09-23 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='valor',
        ),
    ]