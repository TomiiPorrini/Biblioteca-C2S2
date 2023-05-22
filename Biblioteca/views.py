from django.shortcuts import render
from .models import Empleado


def empleados(request):
    empleados = Empleado.objects.all()

    return render(request, 'listado-empleados.html', {'empleados': empleados})

