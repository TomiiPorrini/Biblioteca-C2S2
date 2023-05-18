from django.db import models

# Create your models here.
class autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

class libro(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    isbn = models.IntegerField()
    autor = models.ForeignKey(autor, on_delete=models.SET_NULL, null=True)
    activo = models.BooleanField(default=True)

class socio(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField()

class empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_legajo = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

class prestamoLibro(models.Model):
    fecha_prestamos = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(auto_now_add=True)
    socio = models.ForeignKey(socio, on_delete=models.SET_NULL, null=True)
    empleado = models.ForeignKey(empleado, on_delete=models.SET_NULL, null=True)
    libro = models.ForeignKey(libro, on_delete=models.SET_NULL, null=True)