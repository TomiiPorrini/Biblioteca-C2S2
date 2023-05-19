from django.shortcuts import render, redirect, get_object_or_404
from .models import empleado
from .forms import empleadoForm
# Create your views here.

def crear_empleado(request):
    form = empleadoForm()
    
    if request.method == 'POST':
        form = empleadoForm(request.POST)
        if form.is_valid():
            form.save()
            print("Todo salio bien")
        else:
            print("algo salio mal")
    
    return render(request, 'crear-update_empleado.html', {'form': form, 'submit': 'Crear empleado'})


def modificar_empleado(request, id):
    
    empleadoEditar = get_object_or_404(empleado, id = id)

    form = empleadoForm(initial={
        'nombre':empleadoEditar.nombre ,
        'apellido':empleadoEditar.apellido ,
        'numero_legajo':empleadoEditar.numero_legajo
    })
    
    if request.method == 'POST':
        
        form = empleadoForm(request.POST)
        
        if form.is_valid():
            # form.save()
            print("Todo salio bien")
            
            
            empleadoEditar.nombre = form.cleaned_data['nombre']
            empleadoEditar.apellido = form.cleaned_data['apellido']
            empleadoEditar.numero_legajo = form.cleaned_data['numero_legajo']
            
            empleadoEditar.save()
        else:
            print("algo salio mal")

    return render(request, 'crear-update_empleado.html', {'form': form, 'submit': 'Actualizar empleado'})