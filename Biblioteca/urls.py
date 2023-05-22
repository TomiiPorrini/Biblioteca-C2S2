from django.urls import path
from Biblioteca import views


urlpatterns = [
    path('empleados/activar/<int:id>', views.activar_empleado_view),
    path("empleados/nuevo/", views.crear_empleado, name='crear-empleado'),
    path("empleados/modificar/<int:id>", views.modificar_empleado, name='modificar-empleado')
    path('empleado/listado', views.empleados)
]