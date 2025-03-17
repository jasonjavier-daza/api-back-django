from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer as userSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ViewUsersApi(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = userSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SimpleLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            return Response({"message": "Inicio de sesión exitoso"}, status=status.HTTP_200_OK)
        
        return Response({"error": "Usuario o contraseña incorrectos"}, status=status.HTTP_401_UNAUTHORIZED)
