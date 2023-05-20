from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm, EmpleadoActualizarForm
# Create your views here.

def crear_empleado(request):
    form = EmpleadoForm()
    
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            print("Todo salio bien")
        else:
            print("algo salio mal")
    
    return render(request, 'crear-actualizar-empleado.html', {'form': form, 'submit': 'Crear empleado'})


def modificar_empleado(request, id):
    
    empleadoEditar = get_object_or_404(Empleado, id = id)

    form = EmpleadoActualizarForm(initial={
        'nombre':empleadoEditar.nombre ,
        'apellido':empleadoEditar.apellido ,
        'numero_legajo':empleadoEditar.numero_legajo,
        'activo':empleadoEditar.activo })
    
    if request.method == 'POST':
        
        form = EmpleadoForm(request.POST)
        
        if form.is_valid():
            # form.save()
            print("Todo salio bien")
            
            
            empleadoEditar.nombre = form.cleaned_data['nombre']
            empleadoEditar.apellido = form.cleaned_data['apellido']
            empleadoEditar.numero_legajo = form.cleaned_data['numero_legajo']
            empleadoEditar.activo = form.cleaned_data['activo']
            
            empleadoEditar.save()
        else:
            print("algo salio mal")

    return render(request, 'crear-actualizar-empleado.html', {'form': form, 'submit': 'Actualizar empleado'})