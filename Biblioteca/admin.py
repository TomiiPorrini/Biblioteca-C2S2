from django.contrib import admin
from .models import Autor
# Register your models here.

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    """ Registrar la entidad Autor en el admin  """
    list_display = ('id', 'nombre', 'apellido', 'nacionalidad', 'activo')
    search_fields = ('nombre', 'apellido')
    list_filter = ['activo']

class PrestamoLibroAdmin(admin.PrestamoLibro):
    """ Registrar la entidad PrestamoLibro en el admin. """
    list_display = ('fecha_pestammos','fecha_devolucion','socio','empleado','libro')
    search_fields = ('socio','libro','empleado')