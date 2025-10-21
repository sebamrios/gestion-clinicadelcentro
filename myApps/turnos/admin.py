from django.contrib import admin
from .models import Agenda, Turno
from myApps.pacientes.models import Paciente
from myApps.profesionales.models import Profesional
from django.contrib.auth import get_user_model

User = get_user_model()

# ======================
# Admin de Agenda
# ======================
@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('profesional', 'ver_turnos', 'ver_secretarias')
    search_fields = ('profesional__nombre', 'profesional__apellido')
    filter_horizontal = ('secretarias',)  # para seleccionar varias secretarias cómodamente

    def ver_turnos(self, obj):
        return obj.turnos.count()
    ver_turnos.short_description = "Cantidad de turnos"

    def ver_secretarias(self, obj):
        return ", ".join([s.username for s in obj.secretarias.all()])
    ver_secretarias.short_description = "Secretarias a cargo"

# ======================
# Admin de Turno
# ======================
@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('fecha_hora', 'paciente', 'profesional', 'estado', 'creado_por', 'modificado_por', 'historial')
    list_filter = ('estado', 'agenda__profesional', 'fecha_hora')
    search_fields = ('paciente__apellido', 'paciente__nombre', 'paciente__documento')
    readonly_fields = ('created_at', 'updated_at', 'creado_por', 'modificado_por')
    fields = ('paciente', 'agenda', 'fecha_hora', 'estado', 'motivo', 'created_at', 'updated_at', 'creado_por', 'modificado_por')

    # Mostrar profesional a partir de la agenda
    def profesional(self, obj):
        return obj.agenda.profesional
    profesional.admin_order_field = 'agenda__profesional'

    # Mostrar cantidad de turnos previos del paciente
    def historial(self, obj):
        return obj.paciente.turnos.exclude(id=obj.id).count()
    historial.short_description = "Turnos previos"

    # Registrar quién crea y modifica el turno
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.creado_por = request.user
        obj.modificado_por = request.user
        super().save_model(request, obj, form, change)

    # Limitar queryset según usuario
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Profesionales solo ven sus propios turnos
        if hasattr(request.user, 'profesional'):
            return qs.filter(agenda__profesional=request.user.profesional)
        # Secretarias solo ven agendas a las que tienen acceso
        return qs.filter(agenda__secretarias=request.user)