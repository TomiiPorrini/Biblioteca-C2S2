# Generated by Django 4.2.1 on 2023-06-05 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Biblioteca", "0004_alter_prestamolibro_fecha_devolucion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prestamolibro",
            name="fecha_devolucion",
            field=models.DateField(
                default=datetime.datetime(2023, 6, 7, 16, 5, 14, 741000)
            ),
        ),
    ]