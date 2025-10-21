from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'documento', 'fecha_nac', 'telefono', 'obra_social']
        widgets = {
            'fecha_nac': forms.DateInput(attrs={'type': 'date'}),
        }
        