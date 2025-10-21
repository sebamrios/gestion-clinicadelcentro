from django.contrib import admin
from .models import Secretaria, Licencia, TramoLicencia


# --------------------------------------------------------------------------------
class TramoLicenciaInline(admin.TabularInline):
    model = TramoLicencia
    extra = 0
    readonly_fields = ()
    fields = ("fecha_inicio", "fecha_fin", "dias_tomados")
    help_texts = {
        "dias_tomados": "Ingrese los días computables reales (excluyendo fines de semana y feriados)."
    }

# ---------------------------------------------------------------------------------
class LicenciaInline(admin.TabularInline):
    model = Licencia
    extra = 0
    fk_name = "secretaria"
    fields = (
        "tipo", "periodo", "dias_totales",
        "dias_tomados", "dias_pendientes",
        "fecha_inicio_licencia", "fecha_fin_licencia", "suplente"
    )
    readonly_fields = ("dias_tomados", "dias_pendientes")

# ---------------------------------------------------------------------------------
@admin.register(Licencia)
class LicenciaAdmin(admin.ModelAdmin):
    list_display = ("secretaria", "tipo", "periodo", "dias_totales", "dias_tomados", "dias_pendientes")
    list_filter = ("tipo", "periodo")
    search_fields = ("secretaria__usuario__first_name", "secretaria__usuario__last_name")
    inlines = [TramoLicenciaInline]

#-------------------------------------------------------------------------------
@admin.register(Secretaria)
class SecretariaAdmin(admin.ModelAdmin):
    list_display = ("usuario", "documento", "telefono", "fecha_ingreso")
    list_filter = ("fecha_ingreso",)
    search_fields = ("usuario__first_name", "usuario__last_name", "documento")
    inlines = [LicenciaInline]