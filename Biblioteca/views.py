from django.http import HttpResponse
from django.shortcuts import render
from Biblioteca.models import Empleado

# Create your views here.
def activar_empleado_view(request, id):
    empleado = Empleado.objects.filter(id=id).first()
    empleado.activo=True
    empleado.save()
    return HttpResponse(f'<h1>Empleado "{empleado.nombre} {empleado.apellido}" activado correctamente</h1>')
    
