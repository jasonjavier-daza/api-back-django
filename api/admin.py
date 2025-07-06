from django.contrib import admin
from .models import User, Categoria, Marca, Producto, Carrito

admin.site.register(User)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Carrito)
