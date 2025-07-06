from rest_framework import viewsets
from ..models import Carrito
from ..serializers.serializer_car import (
    CarritoSerializer
)

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
