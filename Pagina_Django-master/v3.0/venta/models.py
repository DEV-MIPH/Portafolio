from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, username, correo_electronico, password=None, **extra_fields):
        if not correo_electronico:
            raise ValueError('El correo electrónico debe ser proporcionado')
        correo_electronico = self.normalize_email(correo_electronico)
        usuario = self.model(username=username, correo_electronico=correo_electronico, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, username, correo_electronico, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, correo_electronico, password, **extra_fields)

class Usuario(AbstractUser):
    username = models.CharField(unique=True, max_length=150)
    correo_electronico = models.EmailField(unique=True)
    nombre = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    comuna = models.CharField(max_length=255)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['correo_electronico', 'nombre']

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=100, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre
    

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcular_precio_total(self):
        if self.cantidad is None:
            self.precio_total = self.producto.precio * 1
            self.save()
        else:
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


