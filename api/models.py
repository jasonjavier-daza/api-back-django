from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=50, blank=True, null=True)
    perfil = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    numdoc = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Categoria(models.Model):
    nombre = models.CharField(max_length=150)
    icono = models.CharField(max_length=255)
    subcategorias = models.TextField()
    banner = models.CharField(max_length=255, blank=True, null=True)
    state_banner = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    banner = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    poster = models.CharField(max_length=255)
    precio_ahora = models.DecimalField(max_digits=10, decimal_places=2)
    precio_antes = models.DecimalField(max_digits=10, decimal_places=2)
    video_review = models.URLField()
    info_short = models.TextField()
    detalle = models.TextField()
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    subcategoria = models.CharField(max_length=150)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, blank=True)
    nombre_selector = models.CharField(max_length=150)
    stars = models.PositiveSmallIntegerField(default=0)
    ventas = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class Carrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    selector = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.producto.titulo} x {self.cantidad}"
