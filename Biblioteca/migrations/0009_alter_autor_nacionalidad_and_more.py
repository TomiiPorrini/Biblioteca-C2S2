# Generated by Django 4.2.1 on 2023-06-08 02:36

import datetime
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteca', '0008_alter_prestamolibro_fecha_devolucion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='nacionalidad',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='prestamolibro',
            name='fecha_devolucion',
            field=models.DateField(default=datetime.datetime(2023, 6, 9, 23, 36, 43, 485334)),
        ),
    ]
