from django.db import models

# Create your models here.
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Entrada(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    texto = models.TextField()

    def __str__(self):
        return f"Comentario en '{self.entrada.titulo}'"
