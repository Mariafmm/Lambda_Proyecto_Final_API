# forms.py
from django import forms
from .models import Notas

class NotaForm(forms.ModelForm):
    class Meta:
        model = Notas
        fields = ['titulo', 'descripcion','imagen_url']  # Los campos del formulario
