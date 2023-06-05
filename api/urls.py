from rest_framework import routers
from .api import LibroViewSet, SocioViewSet, EmpleadoViewSet, AutorViewSet

router = routers.DefaultRouter()

router.register('libros', LibroViewSet, 'api-libros')
router.register('socios', SocioViewSet, 'api-socios')
router.register('empleados', EmpleadoViewSet, 'api-empleados')
router.register('autores', AutorViewSet, 'api-autores')

#exportando las urls.
urlpatterns = router.urls