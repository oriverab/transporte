from dataclasses import fields
from django import forms
from .models import buses

class busesForm(forms.ModelForm):
    class Meta:
        model = buses
        fields = ["id","nombre", "placa", "tipo","numero_de_puestos"]