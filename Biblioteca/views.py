from django.shortcuts import render
from django.http import HttpResponse
from .models import Empleado


def desactivar_empleado_view(request, id):
    empleado = Empleado.objects.filter(id=id).first()
    empleado.activo=False
    empleado.save()
    return HttpResponse(f'<h1>Empleado {empleado.nombre} {empleado.apellido} desactivado correctamente</h1>')
