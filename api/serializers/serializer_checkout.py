# serializers.py
import random
import string
from rest_framework import serializers
from ..models import Venta

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

    def create(self, validated_data):
        # Generar número de comprobante (tracking_number)
        tracking_number = 'TRK-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        validated_data['tracking_number'] = tracking_number

        # Guardar y devolver la venta con tracking incluido
        venta = Venta.objects.create(**validated_data)
        return venta
