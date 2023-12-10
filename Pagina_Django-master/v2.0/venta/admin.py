from django.contrib import admin


from .models import Usuario, Administrador, Producto, CarritoDeCompras, Compra

admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Producto)
admin.site.register(CarritoDeCompras)
admin.site.register(Compra)
