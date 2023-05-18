from django.contrib import admin
from .models import autor, libro, prestamoLibro, empleado, socio
# Register your models here.

@admin.register(autor)
class AutorAdmin(admin.ModelAdmin):
    """ Registrar la entidad Autor en el admin  """
    list_display = ('id', 'nombre', 'apellido', 'nacionalidad', 'activo')
    search_fields = ('nombre', 'apellido')
    list_filter = ['activo', 'nacionalidad']
    
@admin.register(empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    """ Registrar la entidad Empleado en el admin  """
    list_display = ('id', 'nombre', 'apellido', 'numero_legajo', 'activo')
    search_fields = ('nombre', 'apellido')
    list_filter = ['activo']

@admin.register(socio)
class SocioAdmin(admin.ModelAdmin):
    """ Registrar la entidad Socio en el admin  """
    list_display = ('id', 'nombre', 'apellido', 'fecha_nacimiento', 'activo')
    search_fields = ('nombre', 'apellido')
    list_filter = ['activo']

@admin.register(libro)
class LibroAdmin(admin.ModelAdmin):
    """ Registrar la entidad Libro en el admin  """
    list_display = ('id', 'titulo', 'descripcion', 'isbn', 'autor', 'activo')
    search_fields = ('titulo',)
    list_filter = ['activo']

@admin.register(prestamoLibro)
class PrestamoLibroAdmin(admin.ModelAdmin):
    """ Registrar la entidad Prestamo de un libro en el admin. """
    list_display = ('id', 'fecha_prestamos','fecha_devolucion','socio','empleado','libro')
    search_fields = ('socio','libro','empleado')