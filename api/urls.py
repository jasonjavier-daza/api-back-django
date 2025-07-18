from django.urls import path, include
from rest_framework import routers

from api.views.view_orders import AdminOrderViewSet
from .views.view_user import UserViewSet
from .views.view_category import CategoriaViewSet
from .views.view_marc import MarcaViewSet
from .views.view_product import ProductoViewSet
from .views.view_car import CarritoViewSet
from .views.view_checkout import CheckoutViewSet
from .views.view_tracking import TrackingViewSet
from .views.view_login import LoginView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'marcas', MarcaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'carritos', CarritoViewSet)
router.register(r'ventas', CheckoutViewSet)
router.register(r'tracking', TrackingViewSet, basename='tracking')
router.register(r'admin/orders', AdminOrderViewSet, basename='admin-orders')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/login/', LoginView.as_view(), name='login'),
]
