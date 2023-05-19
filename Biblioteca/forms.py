from django.forms import ModelForm
from .models import empleado

class empleadoForm(ModelForm):
    class Meta:
        model = empleado
        fields = ['nombre','apellido','numero_legajo']