from django.db import models
from notas.models import Notas
from user.models import User

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    nota = models.ForeignKey(Notas, on_delete=models.CASCADE, related_name="tareas")
    asignado_a = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tareas_asignadas")
    estado = models.BooleanField(default=False) #si es false quiere decir que aun no se completa
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return f"{self.titulo} - {self.asignado_a.username}"