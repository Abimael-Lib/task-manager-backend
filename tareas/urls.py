from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TareaViewSet
from .views import prueba_auth


router = DefaultRouter()
router.register(r'tareas', TareaViewSet, basename='tarea')

urlpatterns = [
    path('', include(router.urls)),
    path('prueba-auth/', prueba_auth),

]