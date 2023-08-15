from django.shortcuts import render, redirect
from .models import Categoria, Entrada
from .forms import CategoriaForm, EntradaForm, BusquedaForm

def home(request):
    categorias = Categoria.objects.all()
    entradas = Entrada.objects.all()
    return render(request, 'blogapp/home.html', {'categorias': categorias, 'entradas': entradas})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'blogapp/agregar_categoria.html', {'form': form})

def agregar_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntradaForm()
    return render(request, 'blogapp/agregar_entrada.html', {'form': form})

def home(request):
    categorias = Categoria.objects.all()
    entradas = Entrada.objects.all()

    form = BusquedaForm(request.GET)
    if form.is_valid():
        busqueda = form.cleaned_data.get('busqueda')
        if busqueda:
            entradas = entradas.filter(titulo__icontains=busqueda)

    return render(request, 'blogapp/home.html', {'categorias': categorias, 'entradas': entradas, 'form': form})