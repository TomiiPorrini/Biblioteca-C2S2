from rest_framework import serializers
from Biblioteca.models import Libro, Socio, Empleado, Autor

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('id', 'titulo', 'autor')
        
class SocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socio
        fields = ('id', 'nombre', 'apellido', 'fecha_nacimiento', 'activo')
        
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id', 'nombre', 'apellido', 'numero_legajo', 'activo')
        
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('id', 'nombre', 'apellido', 'nacionalidad', 'activo')