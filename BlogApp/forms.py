from django import forms
from .models import Categoria, Entrada

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['titulo', 'contenido', 'categoria']

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=100, required=False, label='Buscar')