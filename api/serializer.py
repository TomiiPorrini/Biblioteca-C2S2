from rest_framework import serializers
from Biblioteca.models import Libro, Socio, Empleado, Autor

class LibroSerializer(serializers.ModelSerializer):
    """Serializador de data para la entidad Libro"""
    class Meta:
        model = Libro
        fields = ('id', 'titulo', 'autor')
        
class SocioSerializer(serializers.ModelSerializer):
    """Serializador de data para la entidad Socio"""
    class Meta:
        model = Socio
        fields = ('id', 'nombre', 'apellido', 'fecha_nacimiento', 'activo')
        
class EmpleadoSerializer(serializers.ModelSerializer):
    """Serializador de data para la entidad Empleado"""
    class Meta:
        model = Empleado
        fields = ('id', 'nombre', 'apellido', 'numero_legajo', 'activo')
        
class AutorSerializer(serializers.ModelSerializer):
    """Serializador de data para la entidad Autor"""
    class Meta:
        model = Autor
        fields = ('id', 'nombre', 'apellido', 'nacionalidad', 'activo')