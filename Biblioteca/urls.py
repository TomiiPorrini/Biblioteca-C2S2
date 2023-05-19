from django.urls import path
from Biblioteca import views


urlpatterns = [
    path("empleado/nuevo/", views.crear_empleado, name='crear-empleado'),
    path("empleados/modificar/<int:id>", views.modificar_empleado, name='modificar-empleado')
    
]