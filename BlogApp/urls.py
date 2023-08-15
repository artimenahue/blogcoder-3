from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('agregar_entrada/', views.agregar_entrada, name='agregar_entrada'),
]
