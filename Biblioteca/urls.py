from django.urls import path
from Biblioteca import views


urlpatterns = [
    path("empleado/crear/", views.crear_empleado, name='crear-empleado')
    
]