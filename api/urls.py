from django.urls import path, include
from rest_framework import routers
from .views.view_user import UserViewSet
from .views.view_category import CategoriaViewSet
from .views.view_marc import MarcaViewSet
from .views.view_product import ProductoViewSet
from .views.view_car import CarritoViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'marcas', MarcaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'carritos', CarritoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
