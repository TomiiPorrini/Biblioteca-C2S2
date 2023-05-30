from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmpleadoForm, EmpleadoActualizarForm, SocioForm, SocioActualizarForm
from .models import Empleado, Autor, Socio

# Create your views here.
def empleados(request):
    empleados = Empleado.objects.all()

    return render(request, 'listado-empleados.html', {'empleados': empleados})

def activar_empleado_view(request, id):
    empleado = Empleado.objects.filter(id=id).first()
    empleado.activo=True
    empleado.save()
    return HttpResponse(f'<h1>Empleado "{empleado.nombre} {empleado.apellido}" activado correctamente</h1>')

def desactivar_empleado_view(request, id):
    empleado = Empleado.objects.filter(id=id).first()
    empleado.activo=False
    empleado.save()
    return HttpResponse(f'<h1>Empleado {empleado.nombre} {empleado.apellido} desactivado correctamente</h1>')

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

    return render(request, 'crear-actualizar-empleado.html', {'orm': form, 'submit': 'Actualizar empleado'})

def autores(request):
    autores = Autor.objects.all()
    return render(request, 'listado-autores.html', {'autores': autores})

def crear_autor(request):
    form = AutorForm()
    
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
    
    return render(request, 'crear_autor.html', {'form': form, 'submit': 'Crear Autor'})

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

def modificar_autor(request, id):
    autor = get_object_or_404(Autor, id = id)

    form = AutorActualizarForm(initial={
        'nombre':autor.nombre ,
        'apellido':autor.apellido ,
        'nacionalidad':autor.nacionalidad,
        # 'activo':autor.activo 
        })

    
    if request.method == 'POST':
        form = AutorActualizarForm(request.POST)
        if form.is_valid():
            if form.has_changed():
                print('El form fue modificado')
                # form.save()
                autor.nombre = form.cleaned_data['nombre']
                autor.apellido = form.cleaned_data['apellido']
                autor.nacionalidad = form.cleaned_data['nacionalidad']
                # autor.activo = form.cleaned_data['activo']
                autor.save()
                print("Datos cargados con éxito.")
            else:
                print('No se modifico ningun dato.')
        else:
            print("Hubo un error al cargar los datos del form.")

    return render(request, 'crear_editar_autor.html', {
        'form' : form,
        'submit_value' : "Actualizar Autor"
    })


def socios(request):
    socios = Socio.objects.all()
    return render(request, 'listado_socios.html', {'socios': socios})

def crear_socio(request):
    form = SocioForm()
    if request.method == 'POST':
        form = SocioForm(request.POST)
        form.save()
        form = SocioForm()
        return redirect('socios')
    else:
        print ("Error")

    return render(request, 'crear_actualizar_socio.html', {'form': form, 'submit': 'Crear Socio'})

def modificar_socio(request, id):

    socioEditar = get_object_or_404(Socio, id = id)

    form = SocioActualizarForm(initial = {
        'nombre': socioEditar.nombre,
        'apellido': socioEditar.apellido,
        'fecha_nacimiento': socioEditar.fecha_nacimiento
    })

    if request.method == 'POST':

        form = SocioForm(request.POST)

        if form.is_valid():
            socioEditar.nombre = form.cleaned_data['nombre']
            socioEditar.apellido = form.cleaned_data['apellido']
            socioEditar.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']

            socioEditar.save()
            return redirect('socios')
        else:
            print ('Error algo salio mal')
    return render(request, 'crear_actualizar_socio.html', {'form': form, 'submit': 'Actualizar Socio'})

def eliminar_socio(request, id):
    socio = Socio.objects.filter(id = id).first()
    socio.delete()
    return redirect('socios')

def activar_socio(request,id):
    socio = Socio.objects.filter(id=id).first()
    socio.activo = True
    socio.save()
    return redirect('socios')

def desactivar_socio(request,id):
    socio = Socio.objects.filter(id=id).first()
    socio.activo = False
    socio.save()
    return redirect('socios')