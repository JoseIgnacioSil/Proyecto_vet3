# Generated by Django 4.0.4 on 2022-07-07 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0009_remove_producto_cantidadinventario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='fechaIngreso',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
    ]