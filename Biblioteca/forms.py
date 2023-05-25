from django.forms import ModelForm
from .models import Empleado, Autor

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre','apellido','numero_legajo']
        
class EmpleadoActualizarForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre','apellido','numero_legajo', 'activo']

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'nacionalidad', 'activo']

class AutorActualizarForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        exclude = ['activo']

