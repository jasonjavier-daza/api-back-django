from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from ..models import Venta
from ..serializers.serializer_checkout import VentaSerializer

class TrackingViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'], url_path='(?P<tracking_number>[^/.]+)')
    def retrieve_by_tracking(self, request, tracking_number=None):
        try:
            venta = Venta.objects.get(tracking_number=tracking_number)
            serializer = VentaSerializer(venta)
            return Response(serializer.data)
        except Venta.DoesNotExist:
            return Response({'error': 'Venta no encontrada'}, status=status.HTTP_404_NOT_FOUND)
