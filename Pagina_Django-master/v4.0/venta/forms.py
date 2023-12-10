from django import forms
from .models import Producto, Categoria


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio','stock', 'categoria','imagen']
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre_categoria']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria 
        fields = ['id_categoria', 'nombre_categoria']