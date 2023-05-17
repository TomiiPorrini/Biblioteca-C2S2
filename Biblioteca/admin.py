from django.contrib import admin
from .models import Autor, Libro, PrestamoLibro
# Register your models here.


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    """ Registrar la entidad Autor en el admin  """
    list_display = ('id', 'nombre', 'apellido', 'nacionalidad', 'activo')
    search_fields = ('nombre', 'apellido')
    list_filter = ['activo']
    
@admin.register(PrestamoLibro)
class PrestamoLibroAdmin(admin.PrestamoLibro):
    """ Registrar la entidad PrestamoLibro en el admin. """
    list_display = ('fecha_pestammos','fecha_devolucion','socio','empleado','libro')
    search_fields = ('socio','libro','empleado')

@admin.register(Libro)
class LibroAdmin(admin.ModelLibro):
    list_display = ('titulo', 'descripcion', 'isbn', 'autor', 'activo')
    search_fields = ('autor')
    list_filter = ['activo']
