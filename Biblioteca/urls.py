from django.urls import path
from Biblioteca import views


urlpatterns = [
    
    path('empleado/listado', views.empleados)
]