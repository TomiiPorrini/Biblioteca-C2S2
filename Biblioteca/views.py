from django.shortcuts import render
from .models import empleado


def empleados(request):
    empleados = empleado.objects.all()

    return render(request, 'listado.html', {'empleados': empleados})

