from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializer import LibroSerializer, SocioSerializer, EmpleadoSerializer, AutorSerializer
from Biblioteca.models import Libro, Socio, Empleado, Autor
# Create your views here.

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LibroSerializer

class SocioViewSet(viewsets.ModelViewSet):
    queryset = Socio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SocioSerializer
    
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpleadoSerializer
    
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AutorSerializer