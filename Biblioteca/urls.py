from django.urls import path
from Biblioteca import views


urlpatterns = [
    path('empleados/activar/<int:id>', views.activar_empleado_view),
]