from django.forms import ModelForm
from .models import Autor, Empleado

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre','apellido','numero_legajo']
        
class EmpleadoActualizarForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre','apellido','numero_legajo', 'activo']

class AutorActualizarForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellido','nacionalidad','activo']
