from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from Biblioteca.models import Empleado,Autor
from .forms import EmpleadoForm, EmpleadoActualizarForm


# Create your views here.


def activar_empleado_view(request, id):
    empleado = Empleado.objects.filter(id=id).first()
    empleado.activo=True
    empleado.save()
    return HttpResponse(f'<h1>Empleado "{empleado.nombre} {empleado.apellido}" activado correctamente</h1>')


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

def empleados(request):
    empleados = Empleado.objects.all()

    return render(request, 'listado-empleados.html', {'empleados': empleados})


def activar_autor_view(request, id):
    autor = Autor.objects.filter(id=id).first()
    autor.activo = True
    autor.save()
    return HttpResponse(f'<h1> el Autor {autor.nombre} {autor.apellido} ha sido activado correctamente </h1>')

def desactivar_autor_view(request,id):
    autor = Autor.objects.filter(id=id).first()
    autor.activo = False
    autor.save()
    return HttpResponse(f'<h1> el Autor {autor.nombre} {autor.apellido} ha sido desactivado correctamente </h1>')