from rest_framework import serializers
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from recordatorios.models import Recordatorio
from user.models import User

class RecordatorioSerializer(serializers.ModelSerializer):
    content_type = serializers.SlugRelatedField(
        queryset=ContentType.objects.all(), slug_field="model" # permite que escriban notas o tareas, para buscar el modelo
    )
    usuarios = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all()) # valida si el user existe

    class Meta:
        model = Recordatorio
        fields = '__all__'  
