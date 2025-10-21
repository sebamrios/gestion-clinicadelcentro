from django import forms
from .models import Usuario 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  

# Formulario para registrar un User
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User  # No Usuario aquí
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # opcional, agrega placeholder

# Formulario para completar el perfil (modelo Usuario)
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre', 'apellido', 'fecha_nacimiento', 'pais', 'provincia', 
            'ciudad', 'domicilio', 'codigo_postal', 'telefono', 'celular',
            'documento', 'cuit', 'imagen'
        ]
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

