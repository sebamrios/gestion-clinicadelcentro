from django.contrib import admin
from .models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'documento', 'fecha_nac', 'telefono', 'obra_social')
    search_fields = ('apellido', 'nombre', 'documento', 'telefono', 'obra_social')
    list_filter = ('obra_social',)