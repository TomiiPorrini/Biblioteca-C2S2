from django.urls import path
from Biblioteca import views


urlpatterns = [
    path('empleados/desactivar/<int:id>', views.desactivar_empleado_view),
]