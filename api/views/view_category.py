from rest_framework import viewsets
from ..models import Categoria
from ..serializers.serializer_category import (
    CategoriaSerializer
)

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer