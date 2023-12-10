from .models import Usuario, Producto,CarritoDeCompras, Compra,Categoria
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.humanize.templatetags.humanize import intcomma





# Create your views here.

import random

def inicio(request):
    productos = list(Producto.objects.all())
    random.shuffle(productos)
    productos_aleatorios = productos[:2]  
    categorias = Categoria.objects.all()
    context = {
        "productos_aleatorios": productos_aleatorios,
        "productos": productos,
        "categorias": categorias
    }
    return render(request, 'venta/index.html', context)


def login(request):
    return render(request,'venta/login.html')

def registro(request):
    return render(request,'venta/registro.html')

def nosotros(request):
    return render(request,'venta/nosotros.html')

def contacto(request):
    return render(request,'venta/contacto.html')



def login_view(request):
    return render(request, 'venta/login.html')


@csrf_exempt
def iniciar_sesion_admin(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        password = request.POST['password']
        if usuario == 'admin' and password == 'admin':
            request.session['admin'] = True
            request.session['admin_username'] = usuario
            return redirect('listar_productos')
        else:
            context = {'mensaje_error': 'Usuario o contraseña incorrectos'}
            return render(request,'venta/soyadmin.html',context)
    return render(request, 'venta/soyadmin.html')

@login_required
def agregar_productos(request):
    mensaje = ''
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  
            mensaje = 'Producto creado correctamente'
            form = ProductoForm()  
    else:
        form = ProductoForm()
    context = {'form': form, 'mensaje': mensaje}
    return render(request, 'venta/producto_add.html', context)




@login_required(login_url='iniciar_sesion', redirect_field_name='next')
def agregar_al_carro(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    
    if request.user.is_authenticated:
        usuario = request.user
        carrito, created = CarritoDeCompras.objects.get_or_create(usuario=usuario)
        
        compra = carrito.compras.filter(producto=producto).first()
        if compra:
            compra.cantidad += 1
            compra.calcular_precio_total()
            compra.save()
        else:
            compra = Compra.objects.create(producto=producto, cantidad=1)
            compra.calcular_precio_total()  # Calcula el precio total de la nueva compra
            compra.save()
            carrito.compras.add(compra)
        
        carrito.calcular_cantidad_total()
        carrito.calcular_precio_total()
        carrito.save()
        
    return redirect('ver_carrito')


@login_required(redirect_field_name='next', login_url='iniciar_sesion')
def ver_carrito(request):
    if request.user.is_authenticated:
        usuario = request.user
        carrito = CarritoDeCompras.objects.get(usuario=usuario)
        context = {'carrito': carrito}
        return render(request, 'venta/carrito.html', context)
        
    else:
        return redirect('iniciar_sesion')

def productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'venta/productos.html', context)


def registro_usuario(request):
    if request.method == 'POST':
        correo_electronico = request.POST.get('email')
        username = correo_electronico
        nombre = request.POST.get('nombre')
        contraseña = request.POST.get('password')
        region = request.POST.get('region')
        comuna = request.POST.get('comuna')

        usuario = Usuario(
            username=username,
            correo_electronico=correo_electronico,
            nombre=nombre,
            region=region,
            comuna=comuna
        )
        usuario.set_password(contraseña)
        usuario.save()

        context = {'mensaje_registro': 'Usuario creado correctamente'}
        return render(request, 'venta/registro.html', context)

    return render(request, 'venta/registro.html')




def iniciar_sesion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contrasena = request.POST.get('password')

        usuario = Usuario.objects.filter(correo_electronico=email).first()

        if usuario is not None:
            if check_password(contrasena, usuario.password):
                auth_login(request, usuario)
                return redirect('productos')  
            else:
                context = {'mensaje_error': 'Contraseña incorrecta'}
                return render(request, 'venta/login.html', context)
        else:
            context = {'mensaje_error': 'No se ha registrado este correo'}
            return render(request, 'venta/login.html', context)
    return render(request, 'venta/login.html')

@login_required(login_url='iniciar_sesion', redirect_field_name='next')
def modificar_cantidad_carro(request, compra_id):
    compra = get_object_or_404(Compra, id_compra=compra_id)
    nueva_cantidad = int(request.POST.get('nueva_cantidad'))
    
    if request.user.is_authenticated:
        usuario = request.user
        carrito = CarritoDeCompras.objects.get(usuario=usuario)
        
        if compra in carrito.compras.all():
            if nueva_cantidad > 0:
                compra.cantidad = nueva_cantidad
                compra.calcular_precio_total()
                compra.save()
            else:
                carrito.compras.remove(compra)
                compra.delete()
        
        carrito.calcular_cantidad_total()
        carrito.calcular_precio_total()
        carrito.save()
        
    return redirect('ver_carrito')

@login_required(login_url='iniciar_sesion', redirect_field_name='next')
def eliminar_del_carro(request, compra_id):
    compra = get_object_or_404(Compra, id_compra=compra_id)
    
    if request.user.is_authenticated:
        usuario = request.user
        carrito = CarritoDeCompras.objects.get(usuario=usuario)
        
        if compra in carrito.compras.all():
            carrito.compras.remove(compra)
            compra.delete()
        
        carrito.calcular_cantidad_total()
        carrito.calcular_precio_total()
        carrito.save()
        
    return redirect('ver_carrito')

def categoria(request,categoria):
    productos = Producto.objects.filter(categoria=categoria)
    context = {'productos': productos}
    return render(request, 'venta/categoria.html', context)

@login_required
def listar_productos(request):
    productos = Producto.objects.all()

    context ={
        'productos' : productos
    }
    
    return render(request, 'venta/listar_productos.html', context)

@login_required
def modificar_productos(request, pk):
    try:
        producto = Producto.objects.get(id_producto=pk)
        if producto:
            if request.method == "POST":
                form = ProductoForm(request.POST,instance=producto)
                form.save() #update en la BD
                context={"mensaje":"se actualizó producto","form":form,"producto":producto}
                return render(request,'venta/modificar_producto.html',context)
            else:
                form = ProductoForm(instance=producto)  
                context={"mensaje":"","form":form,"producto":producto}
                return render(request,'venta/modificar_producto.html',context)
    except:
        lista_productos = Producto.objects.all()
        mensaje = "El producto NO existe"
        context={"mensaje":mensaje,"productos":lista_productos}
        return render(request,'venta/listar_productos.html',context)

@login_required
def eliminar_productos(request, pk):
    try:
        producto = Producto.objects.get(id_producto=pk)
        if producto:
            producto.delete() #delete en la BD
            mensaje = "El género se eliminó"
            lista_productos = Producto.objects.all() 
            context = {"productos":lista_productos, "mensaje":mensaje}
            return render(request,'venta/listar_productos.html',context)
    except:
        mensaje = "El producto NO existe"
        lista_productos = Producto.objects.all() 
        context = {"productos":lista_productos, "mensaje":mensaje}
        return render(request,'venta/productos.html',context)
    

@login_required
def listarCategoria(request):
    categoria = Categoria.objects.all()

    context ={
        'categoria' : categoria
    }
    
    return render(request, 'venta/listar_categorias.html', context)