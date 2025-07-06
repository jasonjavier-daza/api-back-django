from rest_framework import serializers
from ..models import Categoria, Marca, Producto
from .serializer_marc import MarcaSerializer
from .serializer_category import CategoriaSerializer


class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    marca = MarcaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(),
        source='categoria',
        write_only=True,
        allow_null=True
    )
    marca_id = serializers.PrimaryKeyRelatedField(
        queryset=Marca.objects.all(),
        source='marca',
        write_only=True,
        allow_null=True
    )

    class Meta:
        model = Producto
        fields = '__all__'