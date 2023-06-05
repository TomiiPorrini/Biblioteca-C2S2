from rest_framework import serializers
from Biblioteca.models import Libro

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('id', 'titulo', 'autor')