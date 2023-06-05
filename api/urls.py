from rest_framework import routers
from .api import LibroViewSet

router = routers.DefaultRouter()

router.register('libros', LibroViewSet, 'api-libros')

#exportando las urls.
urlpatterns = router.urls