from rest_framework import viewsets
from ..models import Venta
from ..serializers.serializer_checkout import VentaSerializer

class AdminOrderViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all().order_by('-created_at')
    serializer_class = VentaSerializer