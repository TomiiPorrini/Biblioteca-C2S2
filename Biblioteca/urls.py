from django.urls import path
from Biblioteca import views


urlpatterns = [
    path("empleados/nuevo/", views.crear_empleado, name='crear-empleado'),
    path('empleados/activar/<int:id>', views.activar_empleado_view, name='activar-empleado'),
    path('empleados/desactivar/<int:id>', views.desactivar_empleado_view, name='desactivar-empleado'),
    path("empleados/modificar/<int:id>", views.modificar_empleado, name='modificar-empleado'),
    path('empleados/eliminar/<int:id>', views.eliminar_empleado, name='eliminar-empleado'),
    path('empleados/listado', views.empleados, name='empleados'),

    path('autores/nuevo', views.crear_autor, name='crear-autor'),
    path('autores/activar/<int:id>', views.activar_autor_view, name='activar-autor'),
    path('autores/desactivar/<int:id>', views.desactivar_autor_view, name='desactivar-autor'),
    path('autores/modificar/<int:id>', views.modificar_autor, name='modificar-autor'),
    path('autores/eliminar/<int:id>', views.eliminar_autor, name='eliminar-autor'),
    path('autores/listado', views.autores, name='autores'),

    path('libros/nuevo', views.crear_libro, name='crear-libro'),
    path('libros/activar/<int:id>', views.activar_libro, name='activar-libro'),
    path('libros/desactivar/<int:id>', views.desactivar_libro, name='desactivar-libro'),
    path('libros/modificar/<int:id>', views.modificar_libro, name='modificar-libro'),
    path('libros/eliminar/<int:id>', views.eliminar_libro, name='eliminar-libro'),
    path('libros/listado', views.libros, name='libros')

    path('socios/nuevo', views.crear_socio, name='crear-socio'),
    path('socios/activar/<int:id>', views.activar_socio, name='activar-socio'),
    path('socios/desactivar/<int:id>', views.desactivar_socio, name='desactivar-socio'),
    path('socios/modificar/<int:id>', views.modificar_socio, name='modificar-socio'),
    path('socios/eliminar/<int:id>', views.eliminar_socio, name='eliminar-socio'),
    path('socios/listado', views.socios, name='socios'),

]