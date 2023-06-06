from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializer import LibroSerializer, SocioSerializer, EmpleadoSerializer, AutorSerializer
from Biblioteca.models import Libro, Socio, Empleado, Autor
# Create your views here.

class LibroViewSet(viewsets.ModelViewSet):
    """Tomará todos los datos de la bdd en el queryset y se serializa la data de los libros"""
    queryset = Libro.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LibroSerializer

class SocioViewSet(viewsets.ModelViewSet):
    """Tomará todos los datos de la bdd en el queryset y se serializa la data de los socios"""
    queryset = Socio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SocioSerializer
    
class EmpleadoViewSet(viewsets.ModelViewSet):
    """Tomará todos los datos de la bdd en el queryset y se serializa la data de los empleados"""
    queryset = Empleado.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpleadoSerializer
    
class AutorViewSet(viewsets.ModelViewSet):
    """Tomará todos los datos de la bdd en el queryset y se serializa la data de los autores"""
    queryset = Autor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AutorSerializer