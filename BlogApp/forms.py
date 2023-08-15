from django import forms
from .models import Categoria, Entrada

#Formulario para agregar una nueva categoría al blog
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

#Formulario para agregar una nueva entrada al blog.
class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['titulo', 'contenido', 'categoria']

#Formulario de búsqueda para buscar entradas en el blog.
class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=100, required=False, label='Buscar')