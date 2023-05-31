from django.forms import ModelForm
from .models import Empleado, Socio

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre','apellido','numero_legajo']
        
class EmpleadoActualizarForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre','apellido','numero_legajo', 'activo']


#Formulario para crear nuevos socios
# el campo activo de Socio por defecto es True
class SocioForm(ModelForm):
    class Meta:
        model = Socio
        fields = ['nombre', 'apellido', 'fecha_nacimiento']

class SocioActualizarForm(ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'
        exclude = ['activo']
