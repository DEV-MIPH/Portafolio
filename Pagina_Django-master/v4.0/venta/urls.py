from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', views.inicio, name=''),
    path('login', views.login, name='login'),
    path('registro', views.registro, name='registro'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('registro_usuario/', views.registro_usuario, name='registro_usuario'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', LogoutView.as_view(template_name='venta/login.html'), name='cerrar_sesion'),
    path('productos/', views.productos, name='productos'),
    path('iniciar_sesion_admin/', LoginView.as_view(template_name='venta/soyadmin.html'), name='iniciar_sesion_admin'),
    path('agregar_productos/', views.agregar_productos, name='agregar_productos'),
    path('agregar_al_carro/<int:producto_id>/', views.agregar_al_carro, name='agregar_al_carro'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('modificar_cantidad_carro/<int:compra_id>/', views.modificar_cantidad_carro, name='modificar_cantidad_carro'),
    path('eliminar_del_carrito/<int:compra_id>/', views.eliminar_del_carro, name='eliminar_del_carro'),
    path('categoria/<str:categoria>/', views.categoria, name='categoria'),
    path('eliminar_productos/<str:pk>',views.eliminar_productos,name ='eliminar_productos'),
    path('modificar_productos/<str:pk>',views.modificar_productos,name ='modificar_productos'),
    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('listarCategorias/', views.listarCategoria, name='listarCategorias'),
    path('agregar_categorias/', views.agregar_categorias, name='agregar_categorias'),
    path('eliminar_categorias/<str:pk>',views.eliminar_categorias,name ='eliminar_categorias'),
    path('modificar_categorias/<str:pk>',views.modificar_categorias,name ='modificar_categorias'),
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
