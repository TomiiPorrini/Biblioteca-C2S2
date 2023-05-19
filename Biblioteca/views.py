from django.shortcuts import render, redirect
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
    
    return render(request, 'crear_empleado.html', {'form': form})