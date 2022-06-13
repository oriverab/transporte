from dataclasses import fields
from django import forms
from .models import usuarios

class usuarioForm(forms.ModelForm):
    class Meta:
        model = usuarios
        fields = ["id","nombre", "apellido", "correo","contraseña"]