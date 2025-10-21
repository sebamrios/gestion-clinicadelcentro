
from django.contrib import admin
from .models import Especialidad, Profesional


class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'especialidad', 'poblacion', 'contacto')
    list_filter = ('especialidad',)
    search_fields = ('nombre_completo', 'especialidad', 'obras_sociales')

admin.site.register(Especialidad)
admin.site.register(Profesional)