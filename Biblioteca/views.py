from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmpleadoForm, EmpleadoActualizarForm, AutorForm, AutorActualizarForm, LibroForm, LibroActualizarForm
from .models import Empleado, Autor, Libro

# Create your views here.

# Empleado
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

def activar_empleado_view(request, id):
    empleado = Empleado.objects.filter(id=id).first()
    empleado.activo=True
    empleado.save()
    return redirect('empleados')

def desactivar_empleado_view(request, id):
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
        else:
            print("algo salio mal")

    return render(request, 'crear-actualizar-empleado.html', {'form': form, 'submit': 'Actualizar empleado'})

def eliminar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('empleados')

# Autor

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

def activar_autor_view(request, id):
    autor = Autor.objects.filter(id=id).first()
    autor.activo = True
    autor.save()
    return redirect('autores')

def desactivar_autor_view(request,id):
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
                print("Datos cargados con éxito.")
            else:
                print('No se modifico ningun dato.')
        else:
            print("Hubo un error al cargar los datos del form.")

    return render(request, 'crear-editar-autor.html', {'form' : form, 'submit' : "Actualizar Autor"})

def eliminar_autor(request, id):
    autor = Autor.objects.get(id=id)
    autor.delete()
    return redirect('autores')



def libros(request):
    libros = Libro.objects.all()
    return render(request, 'listado_libros.html', {'libros': libros})


def crear_libro(request):
    form = LibroForm()
    if request.method == 'POST':
        form = LibroForm(request.POST)
        form.save()
        form = LibroForm()
    else:
        print ("Error")

    return render(request, 'crear_actualizar_libro.html', {'form': form, 'submit': 'Crear Libro'})

def modificar_libro(request, id):

    libroEditar = get_object_or_404(Libro, id = id)

    form = LibroActualizarForm(initial = {
        'titulo': libroEditar.titulo,
        'descripcion': libroEditar.descripcion,
        'isbn':libroEditar.isbn,
        'autor':libroEditar.autor,
        #activo:libroEditar.activo,
    })

    if request.method == 'POST':

        form = LibroForm(request.POST)

        if form.is_valid():
            libroEditar.titulo = form.cleaned_data['titulo']
            libroEditar.descripcion = form.cleaned_data['descripcion']
            libroEditar.isbn = form.cleaned_data['isbn']
            libroEditar.autor = form.cleaned.data['autor']

            libroEditar.save()
        else:
            print ('Error algo salio mal')
    return render(request, 'crear_actualizar_libro.html', {'form': form, 'submit': 'Actualizar Libro'})

def activar_libro(request,id):
    libro = Libro.objects.filter(id=id).first()
    libro.activo = True
    libro.save()
    return HttpResponse(f'<h1> El socio {libro.titulo} {libro.isbn} ha sido activado correctamente </h1>')

def desactivar_libro(request,id):
    libro = Libro.objects.filter(id=id).first()
    libro.activo = False
    libro.save()
    return HttpResponse(f'<h1> El socio {libro.titulo} {libro.isbn} ha sido desactivado correctamente </h1>')