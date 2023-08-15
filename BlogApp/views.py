from django.shortcuts import render, redirect
from .models import Categoria, Entrada
from .forms import CategoriaForm, EntradaForm, BusquedaForm


#Vista para mostrar la pagina de inicio del blog. Muestra la lista de categorias y entradas que cargues. 
# Ademas, se agrego un boton para realizar las busquedas de las categorias y entradas registradas.
def home(request):
    
    categorias = Categoria.objects.all()
    entradas = Entrada.objects.all()
    return render(request, 'blogapp/home.html', {'categorias': categorias, 'entradas': entradas})

#Vista para agregar una nueva categoría al blog.
def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'blogapp/agregar_categoria.html', {'form': form})

#Vista para agregar una nueva entrada al blog.
def agregar_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntradaForm()
    return render(request, 'blogapp/agregar_entrada.html', {'form': form})

#En la misma vista del blog (home) se agrego un buscador
def home(request):
    categorias = Categoria.objects.all()
    entradas = Entrada.objects.all()

    form = BusquedaForm(request.GET)
    if form.is_valid():
        busqueda = form.cleaned_data.get('busqueda')
        if busqueda:
            entradas = entradas.filter(titulo__icontains=busqueda)

    return render(request, 'blogapp/home.html', {'categorias': categorias, 'entradas': entradas, 'form': form})