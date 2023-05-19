from django.urls import path
from Biblioteca import views


urlpatterns = [
    path("empleado/nuevo/", views.crear_empleado, name='crear-empleado')
    
]