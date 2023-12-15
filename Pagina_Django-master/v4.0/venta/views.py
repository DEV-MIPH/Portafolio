from .models import Usuario, Producto,CarritoDeCompras, Compra,Categoria
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password
from .forms import ProductoForm, CategoriaForm
from .forms import ProductoForm, CategoriaForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login

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

def carrito (request):
    categorias = Categoria.objects.all()
    context = {"categorias": categorias}
    return render(request,'venta/carrito.html',context)
def login(request):
    categorias = Categoria.objects.all()
    context = {"categorias": categorias}
    return render(request,'venta/login.html',context)

def registro(request):
    categorias = Categoria.objects.all()
    context = {"categorias": categorias}
    return render(request,'venta/registro.html',context)

def nosotros(request):
    categorias = Categoria.objects.all()
    context = {"categorias": categorias}
    return render(request,'venta/nosotros.html',context)

def contacto(request):
    categorias = Categoria.objects.all()
    context = {"categorias": categorias}
    return render(request,'venta/contacto.html',context)



def login_view(request):
    categorias = Categoria.objects.all()
    context = {"categorias": categorias}
    return render(request, 'venta/login.html', context)



@csrf_exempt
def iniciar_sesion_admin(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        usuario = request.POST['usuario']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('listar_productos')  
        else:
            context = {'mensaje_error': 'Usuario o contraseña incorrectos', "categorias": categorias}
            return render(request, 'venta/soyadmin.html', context)
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('listar_productos')
    else:
        return render(request, 'venta/soyadmin.html', {"categorias": categorias})



@login_required
def agregar_productos(request):
    mensaje = ''
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            mensaje = 'Producto creado correctamente'
            form = ProductoForm()  
    else:
        form = ProductoForm()
    categoria = Categoria.objects.all()
    context = {'form': form, 'mensaje': mensaje,"categorias": categoria}

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
            compra.calcular_precio_total()  
            compra.save()
            carrito.compras.add(compra)
        
        carrito.calcular_cantidad_total()
        carrito.calcular_precio_total()
        carrito.save()
        
    return redirect('ver_carrito')


@login_required(redirect_field_name='next', login_url='iniciar_sesion')
def ver_carrito(request):
    categorias = Categoria.objects.all()
    if request.user.is_authenticated:
        usuario = request.user
        carrito = CarritoDeCompras.objects.get(usuario=usuario)
        context = {'carrito': carrito,"categorias": categorias}
        return render(request, 'venta/carrito.html', context)
        
    else:
        return redirect('iniciar_sesion')

def productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    context = {'productos': productos,"categorias": categorias}
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
        
        carrito = CarritoDeCompras(usuario=usuario)
        carrito.save()

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
    cantidad = compra.cantidad
    accion = request.POST.get('accion')

    if accion == 'sumar':
        cantidad += 1
    elif accion == 'restar':
        if cantidad > 1:
            cantidad -= 1
        else:
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
            

    compra.cantidad = cantidad
    compra.calcular_precio_total()
    compra.save()

    carrito = CarritoDeCompras.objects.get(usuario=request.user)
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
    nombre_categoria = Categoria.objects.get(id_categoria=categoria)
    categorias = Categoria.objects.all()
    context = {'productos': productos,"nombre_categoria": nombre_categoria,"categorias": categorias}
    return render(request, 'venta/categoria.html', context)

@login_required
def listar_productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    context ={
        'productos' : productos,
        'categorias' : categorias
    }
    
    return render(request, 'venta/listar_productos.html', context)


@login_required
def modificar_productos(request, pk):
    categorias = Categoria.objects.all()
    try:
        producto = Producto.objects.get(id_producto=pk)
        if producto:
            if request.method == "POST":
                form = ProductoForm(request.POST, request.FILES, instance=producto)
                if form.is_valid():
                    form.save()
                    mensaje = "Se actualizó el producto"
                    context = {"mensaje": mensaje, "form": form, "producto": producto, "categorias": categorias}
                    return render(request, 'venta/modificar_producto.html', context)
            else:
                form = ProductoForm(instance=producto)
            context = {"mensaje": "", "form": form, "producto": producto}
            return render(request, 'venta/modificar_producto.html', context)
    except Producto.DoesNotExist:
        lista_productos = Producto.objects.all()
        mensaje = "El producto NO existe"
        context = {"mensaje": mensaje, "productos": lista_productos, "categorias": categorias}
        return render(request, 'venta/listar_productos.html', context)




@login_required
def eliminar_productos(request, pk):
    categorias = Categoria.objects.all()
    try:
        producto = Producto.objects.get(id_producto=pk)
        if producto:
            producto.delete() #delete en la BD
            mensaje = "El género se eliminó"
            lista_productos = Producto.objects.all() 
            context = {"productos":lista_productos, "mensaje":mensaje, "categorias": categorias}
            return render(request,'venta/listar_productos.html',context)
    except:
        mensaje = "El producto NO existe"
        lista_productos = Producto.objects.all() 
        context = {"productos":lista_productos, "mensaje":mensaje, "categorias": categorias}
        return render(request,'venta/productos.html',context)
@login_required
def agregar_categoria(request):
    mensaje_categoria= ''
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje_categoria = 'Categoría creada correctamente'
            form = CategoriaForm()
    else:
        form = CategoriaForm()
    
    categorias = Categoria.objects.all()
    context = {'form': form, 'mensaje_categoria': mensaje_categoria, 'categorias': categorias}
    return render(request, 'venta/producto_add.html', context)

    
@login_required
def listarCategoria(request):
    categorias = Categoria.objects.all()

    context ={
        'categoria' : categorias,
        "categorias": categorias
    }
    
    return render(request, 'venta/listar_categorias.html', context)


@login_required
def agregar_categorias(request):
    categorias = Categoria.objects.all()
    mensaje = ''
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            mensaje = 'Producto creado correctamente'
            form = CategoriaForm()  
    else:
        form = CategoriaForm()
    context = {'form': form, 'mensaje': mensaje, 'categorias': categorias}
    return render(request, 'venta/categorias_add.html', context)


@login_required
def modificar_categorias(request, pk):
    categorias = Categoria.objects.all()
    try:
        categoria = Categoria.objects.get(id_categoria=pk)
        if categoria:
            if request.method == "POST":
                form = CategoriaForm(request.POST,instance=categoria)
                form.save() #update en la BD
                context={"mensaje":"se actualizó categoria","form":form,"categoria":categoria}
                return render(request,'venta/modificar_categorias.html',context)
            else:
                form = CategoriaForm(instance=categoria)  
                context={"mensaje":"","form":form,"categoria":categoria, "categorias": categorias}
                return render(request,'venta/modificar_categorias.html',context)
    except:
        lista_categorias = Categoria.objects.all()
        mensaje = "la categoria NO existe"
        context={"mensaje":mensaje,"productos":lista_categorias, "categorias": categorias}
        return render(request,'venta/listar_categorias.html',context)

@login_required
def eliminar_categorias(request, pk):
    try:
        categoria = Categoria.objects.get(id_categoria=pk)
        categorias = Categoria.objects.all()
        if categoria:
            categoria.delete() 
            mensaje = "la categoria se eliminó"
            lista_categoria = Categoria.objects.all() 
            context = {"categoria":lista_categoria, "mensaje":mensaje,"categorias":categorias}
            return render(request,'venta/listar_categorias.html',context)
    except:
        mensaje = "La categoria NO existe"
        lista_categoria = Categoria.objects.all() 
        context = {"categoria":lista_categoria, "mensaje":mensaje,"categoria":lista_categoria, "categorias": categorias}
        return render(request,'venta/categoria.html',context)
