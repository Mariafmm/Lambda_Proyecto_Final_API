from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre_categoria")
    description = models.TextField(blank=True, null=True, verbose_name="Descripcion")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha_creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha_actualizacion") 

    def __str__(self):
        return self.name

class Notas(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen_url = models.URLField(max_length=200, blank=True, null=True)
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="notas")
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.titulo
    
    
