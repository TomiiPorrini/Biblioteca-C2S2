from django.urls import path
from Biblioteca import views


urlpatterns = [
    path('empleados/desactivar/<int:id>', views.desactivar_empleado_view),
    path('empleados/activar/<int:id>', views.activar_empleado_view, name='activar-empleado'),
    path("empleados/nuevo/", views.crear_empleado, name='crear-empleado'),
    path("empleados/modificar/<int:id>", views.modificar_empleado, name='modificar-empleado'),
    path("empleados/modificar/<int:id>", views.modificar_empleado, name='modificar-empleado'),
    path('empleados/listado', views.empleados),
    path('autores/listado', views.autores),
    path('autores/modificar/<int:id>', views.modificar_autor, name='modificar-autor')
]