from django.urls import path
from Biblioteca import views


urlpatterns =[
    path('/empleados/listado', views.Personas)
]