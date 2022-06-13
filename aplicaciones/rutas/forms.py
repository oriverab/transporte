from dataclasses import fields
from django import forms
from .models import rutas

class rutasForm(forms.ModelForm):
    class Meta:
        model = rutas
        fields = ["id","nombre", "ciudad_origen", "ciudad_destino"]