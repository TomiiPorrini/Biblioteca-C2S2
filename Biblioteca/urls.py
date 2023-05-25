from django.urls import path
from Biblioteca import views


urlpatterns = [
    path("empleados/nuevo/", views.crear_empleado, name='crear-empleado'),
    path('empleados/activar/<int:id>', views.activar_empleado_view),
    path('empleados/desactivar/<int:id>', views.desactivar_empleado_view),
    path("empleados/modificar/<int:id>", views.modificar_empleado, name='modificar-empleado'),
    path('empleados/listado', views.empleados),

    path('autores/nuevo', views.crear_autor, name='crear-autor'),
    path('autores/activar/<int:id>', views.activar_autor_view),
    path('autores/desactivar/<int:id>', views.desactivar_autor_view),
    path('autores/modificar/<int:id>', views.modificar_autor, name='modificar-autor'),
    path('autores/listado', views.autores),
]