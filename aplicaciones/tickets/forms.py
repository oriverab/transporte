from dataclasses import fields
from django import forms
from .models import tickets

class ticketsForm(forms.ModelForm):
    class Meta:
        model = tickets
        fields = '__all__'
        widgets = {
            'id': forms.Select(attrs={
                'class': "form-control",
                'placeholder': "Seleccione su ruta"
                }),
            'fecha': forms.TextInput(attrs={
                'class': "form-control",
                'onfocus': "(this.type='date')",
                'onblur': "(this.type='text')"
                }),
            'buses_id': forms.Select(attrs={
                'class': "form-control", 
                'placeholder': 'Cootransfusa'
                }),
            'rutas_id': forms.Select(attrs={
                'class': "form-control", 
                'placeholder': 'Pepito Perez'
                }),
            'usuarios_id': forms.Select(attrs={
                'class': "form-control", 
                'placeholder': 'Pepito Perez'
                }),
            'puestos': forms.NumberInput(attrs={
                'class': "form-control", 
                'placeholder': 'numero',
                'max':'40',
                'min':'1',
                }),
            
        }