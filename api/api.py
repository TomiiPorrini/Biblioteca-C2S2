from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializer import LibroSerializer
from Biblioteca.models import Libro
# Create your views here.

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LibroSerializer
