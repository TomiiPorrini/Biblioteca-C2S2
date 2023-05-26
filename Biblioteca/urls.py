from django.urls import path
from Biblioteca import views


urlpatterns = [
    path("empleados/nuevo/", views.crear_empleado, name='crear-empleado'),
    path('empleados/activar/<int:id>', views.activar_empleado_view, name='activar-empleado'),
    path('empleados/desactivar/<int:id>', views.desactivar_empleado_view, name='desactivar-empleado'),
    path("empleados/modificar/<int:id>", views.modificar_empleado, name='modificar-empleado'),
    path('empleados/listado', views.empleados, name='empleados'),

    path('autores/nuevo', views.crear_autor, name='crear-autor'),
    path('autores/activar/<int:id>', views.activar_autor_view, name='activar-autor'),
    path('autores/desactivar/<int:id>', views.desactivar_autor_view, name='desactivar-autor'),
    path('autores/modificar/<int:id>', views.modificar_autor, name='modificar-autor'),
    path('autores/listado', views.autores, name='autores'),
]