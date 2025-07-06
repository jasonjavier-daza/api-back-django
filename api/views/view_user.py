from rest_framework import viewsets
from ..models import User
from ..serializers.serializer_user import (
    UserSerializer
)

class UserViewSet(# In this Python code snippet, `viewsets` is a module imported from the
# `rest_framework` package. It provides a way to create full-featured CRUD (Create,
# Read, Update, Delete) views for models in a Django REST framework API.
viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer