from django.forms import ModelForm
from django import forms
from .models import Empleado, Autor, Libro, Socio, PrestamoLibro


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre','apellido','numero_legajo']
        
class EmpleadoActualizarForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre','apellido','numero_legajo']

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'nacionalidad']

class AutorActualizarForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        exclude = ['activo']

#Formulario para crear nuevos socios
# el campo activo de Socio por defecto es True


class SocioForm(ModelForm):
    class Meta:
        model = Socio
        fields = ['nombre', 'apellido', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
        }

class SocioActualizarForm(ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'
        exclude = ['activo']

class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'descripcion', 'isbn', 'autor']

class LibroActualizarForm(ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        exclude = ['activo']

class PrestamoForm(ModelForm):
    class Meta:
        model = PrestamoLibro
        fields = '__all__'
        exclude = ['fecha_devolucion']

class PrestamoActualizarForm(ModelForm):
    class Meta:
        model = PrestamoLibro
        fields = '__all__'
        exclude = ['fecha_devolucion']