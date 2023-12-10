from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    correo_electronico = models.EmailField()
    nombre = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    comuna = models.CharField(max_length=255)
    last_login = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
    def usuario_conectado(self):
        return self
    
class Administrador(models.Model):
    id_admin = models.AutoField(primary_key=True)
    correo_electronico = models.EmailField()
    nombre = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=100, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)


    def __str__(self):
        return self.nombre
    

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcular_precio_total(self):
        self.precio_total = self.producto.precio * self.cantidad
        self.save()

    def __str__(self):
        return f"Compra {self.id_compra} para el producto {self.producto.nombre}"

class CarritoDeCompras(models.Model):
    id_carrito = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    compras = models.ManyToManyField(Compra)
    cantidad_total = models.PositiveIntegerField(default=0)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcular_cantidad_total(self):
        self.cantidad_total = self.compras.count()
        self.save()

    def calcular_precio_total(self):
        self.precio_total = sum(compra.precio_total for compra in self.compras.all())
        self.save()

    def __str__(self):
        return f"Carrito de compras {self.id_carrito} para el usuario {self.usuario.nombre}"


