from django.shortcuts import render
from models import Persona
# Create your views here.

def Empleados(request):
    empleados = Persona.objects.all()

    return render(request, 'listado', {'empleados': empleados})

