from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmpleadoForm, EmpleadoActualizarForm, AutorForm, AutorActualizarForm, LibroForm, LibroActualizarForm, SocioForm, SocioActualizarForm, PrestamoForm, PrestamoActualizarForm
from .models import Empleado, Autor, Libro, Socio, PrestamoLibro
from datetime import date
# Create your views here.

# EMPLEADOS

def empleados(request):
    empleados = Empleado.objects.all()

    return render(request, 'listado-empleados.html', {'empleados': empleados})

def crear_empleado(request):
    form = EmpleadoForm()
    
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados')

    
    return render(request, 'crear-actualizar-empleado.html', {'form': form, 'submit': 'Crear empleado'})

def activar_empleado(request, id):
    empleado = Empleado.objects.filter(id=id).first()
    empleado.activo=True
    empleado.save()
    return redirect('empleados')

def desactivar_empleado(request, id):
    empleado = Empleado.objects.filter(id=id).first()
    empleado.activo=False
    empleado.save()
    return redirect('empleados')

def modificar_empleado(request, id):
    
    empleadoEditar = get_object_or_404(Empleado, id = id)

    form = EmpleadoActualizarForm(initial={
        'nombre':empleadoEditar.nombre ,
        'apellido':empleadoEditar.apellido ,
        'numero_legajo':empleadoEditar.numero_legajo,
        })
    
    if request.method == 'POST':
        
        form = EmpleadoForm(request.POST)
        
        if form.is_valid():
            # form.save()
            print("Todo salio bien")
            
            
            empleadoEditar.nombre = form.cleaned_data['nombre']
            empleadoEditar.apellido = form.cleaned_data['apellido']
            empleadoEditar.numero_legajo = form.cleaned_data['numero_legajo']
            
            empleadoEditar.save()
            return redirect('empleados')
        else:
            print("algo salio mal")

    return render(request, 'crear-actualizar-empleado.html', {'form': form, 'submit': 'Actualizar empleado'})

def eliminar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('empleados')

# AUTORES

def autores(request):
    autores = Autor.objects.all()
    return render(request, 'listado-autores.html', {'autores': autores})

def crear_autor(request):
    form = AutorForm()
    
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autores')
    
    return render(request, 'crear-editar-autor.html', {'form': form, 'submit': 'Crear Autor'})

def activar_autor(request, id):
    autor = Autor.objects.filter(id=id).first()
    autor.activo = True
    autor.save()
    return redirect('autores')

def desactivar_autor(request,id):
    autor = Autor.objects.filter(id=id).first()
    autor.activo = False
    autor.save()
    return redirect('autores')

def modificar_autor(request, id):
    autor = get_object_or_404(Autor, id = id)

    form = AutorActualizarForm(initial={
        'nombre':autor.nombre ,
        'apellido':autor.apellido ,
        'nacionalidad':autor.nacionalidad,
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
                autor.save()
                #print("Datos cargados con éxito.")
                return redirect('autores')
        else:
                print("Hubo un error al cargar los datos del form.")

    return render(request, 'crear-editar-autor.html', {
        'form' : form,
        'submit' : "Actualizar Autor"})

def eliminar_autor(request, id):
    autor = Autor.objects.get(id=id)
    autor.delete()
    return redirect('autores')

# SOCIOS

def socios(request):
    socios = Socio.objects.all()
    return render(request, 'listado-socios.html', {'socios': socios})

def crear_socio(request):
    form = SocioForm()
    if request.method == 'POST':
        form = SocioForm(request.POST)
        form.save()
        form = SocioForm()
        return redirect('socios')
    else:
        print ("Error")

    return render(request, 'crear-actualizar-socio.html', {'form': form, 'submit': 'Crear Socio'})

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
    return render(request, 'crear-actualizar-socio.html', {'form': form, 'submit': 'Actualizar Socio'})

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


# LIBROS

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'listado-libros.html', {'libros': libros})

def crear_libro(request):
    form = LibroForm()
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libros')

    else:
        print ("Error")

    return render(request, 'crear-actualizar-libro.html', {'form': form, 'submit': 'Crear Libro'})

def modificar_libro(request, id):

    libroEditar = get_object_or_404(Libro, id = id)

    form = LibroActualizarForm(initial = {
        'titulo': libroEditar.titulo,
        'descripcion': libroEditar.descripcion,
        'isbn':libroEditar.isbn,
        'autor':libroEditar.autor,
    })

    if request.method == 'POST':

        form = LibroForm(request.POST)

        if form.is_valid():
            libroEditar.titulo = form.cleaned_data['titulo']
            libroEditar.descripcion = form.cleaned_data['descripcion']
            libroEditar.isbn = form.cleaned_data['isbn']
            libroEditar.autor = form.cleaned_data['autor']

            libroEditar.save()
            return redirect('libros')
        else:
            print ('Error algo salio mal')
    return render(request, 'crear-actualizar-libro.html', {'form': form, 'submit': 'Actualizar Libro'})

def activar_libro(request,id):
    libro = Libro.objects.filter(id=id).first()
    libro.activo = True
    libro.save()
    return redirect('libros')

def desactivar_libro(request,id):
    libro = Libro.objects.filter(id=id).first()
    libro.activo = False
    libro.save()
    return redirect('libros')

def eliminar_libro(request, id):
    libros = Libro.objects.get(id=id)
    libros.delete()
    return redirect('libros')

# PRESTAMOS LIBROS

def prestamos(request):
    prestamos = PrestamoLibro.objects.all()

    return render(request, 'listado-prestamos.html', {'prestamos': prestamos})

def crear_prestamo(request):
    form = PrestamoForm()
    
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid() and form.cleaned_data['socio'].activo and form.cleaned_data['empleado'].activo and form.cleaned_data['libro'].activo:
            form.save()

            return redirect('prestamos')
        else:
            print('no se pudo')

    
    return render(request, 'crear-actualizar-prestamo.html', {'form': form, 'submit': 'Crear prestamo'})


def modificar_prestamo(request, id):
    
    prestamoEditar = get_object_or_404(PrestamoLibro, id = id)

    form = PrestamoActualizarForm(initial={
        
        'socio':prestamoEditar.socio,
        'empleado':prestamoEditar.empleado,
        'libro':prestamoEditar.libro
        })
    
    if request.method == 'POST':
        
        form = PrestamoForm(request.POST)
        
        if form.is_valid() and form.cleaned_data['socio'].activo and form.cleaned_data['empleado'].activo and form.cleaned_data['libro'].activo:
            
            print("Todo salio bien")
            prestamoEditar.socio = form.cleaned_data['socio']
            prestamoEditar.empleado = form.cleaned_data['empleado']
            prestamoEditar.libro = form.cleaned_data['libro']
            
            prestamoEditar.save()
            return redirect('prestamos')
        else:
            print("algo salio mal")

    return render(request, 'crear-actualizar-prestamo.html', {'form': form, 'submit': 'Actualizar Prestamo'})

def eliminar_prestamo(request, id):
    prestamo = PrestamoLibro.objects.get(id=id)
    prestamo.delete()
    return redirect('prestamos')
