from django.db import models

# Create your models here.


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_legajo = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

class PrestamoLibro(models.Model):
    fecha_prestamos = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(auto_now_add=True)
    socio = models.ForeignKey(Socio)
    empleado = models.ForeignKey(Empleado)
    libro = models.ForeignKey(Libro)

