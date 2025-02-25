from rest_framework import serializers
from .models import Notas, Category

class NotaSerializer(serializers.ModelSerializer):
    categoria = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Notas
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'