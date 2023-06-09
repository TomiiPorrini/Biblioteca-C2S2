from rest_framework import routers
from .api import LibroViewSet, SocioViewSet, EmpleadoViewSet, AutorViewSet

#Se crea el router que nos va a crear las urls de cada viewset
router = routers.DefaultRouter()


#Registramos cada viewset a nuestro router y les ponemos un nombre 
router.register('libros', LibroViewSet, 'api-libros')
router.register('socios', SocioViewSet, 'api-socios')
router.register('empleados', EmpleadoViewSet, 'api-empleados')
router.register('autores', AutorViewSet, 'api-autores')

#Exportamos las urls al urls.py principal del proyecto.
urlpatterns = router.urls
    