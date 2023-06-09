from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmpleadoForm, EmpleadoActualizarForm, AutorForm, AutorActualizarForm, LibroForm, LibroActualizarForm, SocioForm, SocioActualizarForm, PrestamoForm, PrestamoActualizarForm
from .models import Empleado, Autor, Libro, Socio, PrestamoLibro
from datetime import date
# Create your views here.

# EMPLEADOS

def campos_validos_empleado(formulario):
    return formulario.cleaned_data['nombre'].isalpha() and formulario.cleaned_data['apellido'].isalpha() and formulario.cleaned_data['numero_legajo'].isnumeric()
        
def empleados(request):
    """Obtiene todos los datos de la entidad y los muestra en un listado"""
    empleados = Empleado.objects.all()

    return render(request, 'listado-empleados.html', {'empleados': empleados})

def crear_empleado(request):
    """Crea una la entidad empleado por medio de un formulario donde obtiene sus datos."""
    form = EmpleadoForm()
    
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid() and campos_validos_empleado(form):
            form.save()
            return redirect('empleados')
    
    return render(request, 'crear-actualizar-empleado.html', {'form': form, 'submit': 'Crear empleado'})

def activar_empleado(request, id):
    """coloca el valor True en el campo activo de la entidad."""
    empleado = Empleado.objects.filter(id=id).first()
    empleado.activo=True
    empleado.save()
    return redirect('empleados')

def desactivar_empleado(request, id):
    """coloca el valor False en el campo activo de la entidad."""
    empleado = Empleado.objects.filter(id=id).first()
    empleado.activo=False
    empleado.save()
    return redirect('empleados')

def modificar_empleado(request, id):
    """Modifica los datos de una entidad existente por medio de un formulario"""
    empleadoEditar = get_object_or_404(Empleado, id = id)

    form = EmpleadoActualizarForm(initial={
        'nombre':empleadoEditar.nombre ,
        'apellido':empleadoEditar.apellido ,
        'numero_legajo':empleadoEditar.numero_legajo,
        })
    
    if request.method == 'POST':
        
        form = EmpleadoForm(request.POST)
        
        if form.is_valid() and campos_validos_empleado(form):
            
            empleadoEditar.nombre = form.cleaned_data['nombre']
            empleadoEditar.apellido = form.cleaned_data['apellido']
            empleadoEditar.numero_legajo = form.cleaned_data['numero_legajo']
            empleadoEditar.save()
            return redirect('empleados')
        else:
            print("algo salio mal")

    return render(request, 'crear-actualizar-empleado.html', {'form': form, 'submit': 'Actualizar empleado'})

def eliminar_empleado(request, id):
    """Elimina un registro de la entidad empleado"""
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('empleados')

# AUTORES

def campos_validos_autor(formulario):
    return formulario.cleaned_data['nombre'].isalpha() and formulario.cleaned_data['apellido'].isalpha() and formulario.cleaned_data['nacionalidad'].isalpha()

def autores(request):
    """Obtiene todos los datos de la entidad y los muestra en un listado"""
    autores = Autor.objects.all()
    return render(request, 'listado-autores.html', {'autores': autores})

def crear_autor(request):
    """Crea una la entidad autor por medio de un formulario donde obtiene sus datos."""
    form = AutorForm()
    
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid() and campos_validos_autor(form):
            form.save()
            return redirect('autores')
    
    return render(request, 'crear-editar-autor.html', {'form': form, 'submit': 'Crear Autor'})

def activar_autor(request, id):
    """coloca el valor True en el campo activo de la entidad."""
    autor = Autor.objects.filter(id=id).first()
    autor.activo = True
    autor.save()
    return redirect('autores')

def desactivar_autor(request,id):
    """coloca el valor False en el campo activo de la entidad."""
    autor = Autor.objects.filter(id=id).first()
    autor.activo = False
    autor.save()
    return redirect('autores')

def modificar_autor(request, id):
    """Modifica los datos de una entidad existente por medio de un formulario"""
    autor = get_object_or_404(Autor, id = id)

    form = AutorActualizarForm(initial={
        'nombre':autor.nombre ,
        'apellido':autor.apellido ,
        'nacionalidad':autor.nacionalidad,
        })

    
    if request.method == 'POST':
        form = AutorActualizarForm(request.POST)
        if form.is_valid():
            if form.has_changed() and campos_validos_autor(form):
                
                autor.nombre = form.cleaned_data['nombre']
                autor.apellido = form.cleaned_data['apellido']
                autor.nacionalidad = form.cleaned_data['nacionalidad']
                autor.save()
                return redirect('autores')
        else:
                print("Hubo un error al cargar los datos del form.")

    return render(request, 'crear-editar-autor.html', {
        'form' : form,
        'submit' : "Actualizar Autor"})

def eliminar_autor(request, id):
    """Elimina un registro de la entidad autor"""
    autor = Autor.objects.get(id=id)
    autor.delete()
    return redirect('autores')

# SOCIOS

def campos_validos_socio(formulario):
    return formulario.cleaned_data['nombre'].isalpha() and formulario.cleaned_data['apellido'].isalpha()

def socios(request):
    """Obtiene todos los datos de la entidad y los muestra en un listado"""
    socios = Socio.objects.all()
    return render(request, 'listado-socios.html', {'socios': socios})

def crear_socio(request):
    """Crea una la entidad socio por medio de un formulario donde obtiene sus datos."""
    form = SocioForm()
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid() and campos_validos_socio(form):
            form.save()

        return redirect('socios')
    else:
        print("Error")

    return render(request, 'crear-actualizar-socio.html', {'form': form, 'submit': 'Crear Socio'})

def modificar_socio(request, id):
    """Modifica los datos de una entidad existente por medio de un formulario"""
    socioEditar = get_object_or_404(Socio, id = id)

    form = SocioActualizarForm(initial = {
        'nombre': socioEditar.nombre,
        'apellido': socioEditar.apellido,
        'fecha_nacimiento': socioEditar.fecha_nacimiento
    })

    if request.method == 'POST':

        form = SocioForm(request.POST)

        if form.is_valid() and campos_validos_socio(form):
            socioEditar.nombre = form.cleaned_data['nombre']
            socioEditar.apellido = form.cleaned_data['apellido']
            socioEditar.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']

            socioEditar.save()
            return redirect('socios')
        else:
            print('Error algo salio mal')
    return render(request, 'crear-actualizar-socio.html', {'form': form, 'submit': 'Actualizar Socio'})

def eliminar_socio(request, id):
    """Elimina un registro de la entidad socio"""
    socio = Socio.objects.filter(id = id).first()
    socio.delete()
    return redirect('socios')

def activar_socio(request,id):
    """coloca el valor True en el campo activo de la entidad."""
    socio = Socio.objects.filter(id=id).first()
    socio.activo = True
    socio.save()
    return redirect('socios')

def desactivar_socio(request,id):
    """coloca el valor False en el campo activo de la entidad."""
    socio = Socio.objects.filter(id=id).first()
    socio.activo = False
    socio.save()
    return redirect('socios')  

# LIBROS

def libros(request):
    """Obtiene todos los datos de la entidad y los muestra en un listado"""
    libros = Libro.objects.all()
    return render(request, 'listado-libros.html', {'libros': libros})

def crear_libro(request):
    """Crea una la entidad libro por medio de un formulario donde obtiene sus datos."""
    form = LibroForm()
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libros')

    else:
        print("Error")

    return render(request, 'crear-actualizar-libro.html', {'form': form, 'submit': 'Crear Libro'})

def modificar_libro(request, id):
    """Modifica los datos de una entidad existente por medio de un formulario"""
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
            print('Error algo salio mal')
    return render(request, 'crear-actualizar-libro.html', {'form': form, 'submit': 'Actualizar Libro'})

def activar_libro(request,id):
    """coloca el valor True en el campo activo de la entidad."""
    libro = Libro.objects.filter(id=id).first()
    libro.activo = True
    libro.save()
    return redirect('libros')

def desactivar_libro(request,id):
    """coloca el valor False en el campo activo de la entidad."""
    libro = Libro.objects.filter(id=id).first()
    libro.activo = False
    libro.save()
    return redirect('libros')

def eliminar_libro(request, id):
    """Elimina un registro de la entidad libro"""
    libros = Libro.objects.get(id=id)
    libros.delete()
    return redirect('libros')

# PRESTAMOS LIBROS

def campos_validos_prestamo(formulario):
    return formulario.cleaned_data['socio'].activo and formulario.cleaned_data['empleado'].activo and formulario.cleaned_data['libro'].activo

def prestamos(request):
    """Obtiene todos los datos de la entidad y los muestra en un listado"""
    prestamos = PrestamoLibro.objects.all()
    return render(request, 'listado-prestamos.html', {'prestamos': prestamos})

def crear_prestamo(request):
    """Crea una la entidad prestamoLibro por medio de un formulario donde obtiene sus datos."""
    form = PrestamoForm()
    
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid() and campos_validos_prestamo(form):
            form.save()

            return redirect('prestamos')
        else:
            print('no se pudo')

    
    return render(request, 'crear-actualizar-prestamo.html', {'form': form, 'submit': 'Crear prestamo'})

def modificar_prestamo(request, id):
    """Modifica los datos de una entidad existente por medio de un formulario"""
    prestamoEditar = get_object_or_404(PrestamoLibro, id = id)

    form = PrestamoActualizarForm(initial={
        
        'socio':prestamoEditar.socio,
        'empleado':prestamoEditar.empleado,
        'libro':prestamoEditar.libro
        })
    
    if request.method == 'POST':
        
        form = PrestamoForm(request.POST)
        
        if form.is_valid() and campos_validos_prestamo(form):
            
            
            prestamoEditar.socio = form.cleaned_data['socio']
            prestamoEditar.empleado = form.cleaned_data['empleado']
            prestamoEditar.libro = form.cleaned_data['libro']
            
            prestamoEditar.save()
            return redirect('prestamos')
        else:
            print("algo salio mal")

    return render(request, 'crear-actualizar-prestamo.html', {'form': form, 'submit': 'Actualizar Prestamo'})

def eliminar_prestamo(request, id):
    """Elimina un registro de la entidad PrestamoLibro"""
    prestamo = PrestamoLibro.objects.get(id=id)
    prestamo.delete()
    return redirect('prestamos')
