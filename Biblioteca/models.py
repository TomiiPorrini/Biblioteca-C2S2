from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    isbn = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    activo = models.BooleanField(default=True)

class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField()

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_legajo = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

class PrestamoLibro(models.Model):
    fecha_prestamos = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(auto_now_add=True)
    socio = models.ForeignKey(Socio, on_delete=models.SET_NULL, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)
    libro = models.ForeignKey(Libro, on_delete=models.SET_NULL, null=True)