from rest_framework import serializers
from .models import Tarea
from user.models import User
from notas.models import Notas

class TareaSerializer(serializers.ModelSerializer):
    nota = serializers.PrimaryKeyRelatedField(queryset=Notas.objects.all())  #valida si existe
    asignado_a = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    
    class Meta:
        model = Tarea
        fields = "__all__"