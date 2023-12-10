from django.contrib import admin


from .models import Usuario, Producto, CarritoDeCompras, Compra,Categoria

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(CarritoDeCompras)
admin.site.register(Compra)
admin.site.register(Categoria)
