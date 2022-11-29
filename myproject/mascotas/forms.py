from .models import Adopcion
from django import forms

class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = ['nombres', 'apellidos', 'correo', 'cedula', 'direccion', 'fechaNacimiento', 'telefono']