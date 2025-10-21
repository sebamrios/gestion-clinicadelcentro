from django.db import models
from django.contrib.auth import get_user_model
from myApps.profesionales.models import Profesional
from myApps.pacientes.models import Paciente

User = get_user_model()

# ======================
# Modelo Agenda
# ======================
class Agenda(models.Model):
    profesional = models.OneToOneField(Profesional, on_delete=models.CASCADE, related_name='agenda')
    secretarias = models.ManyToManyField(User, blank=True, related_name='agendas_a_cargo')

    def __str__(self):
        return f"Agenda de {self.profesional}"

# ======================
# Modelo Turno
# ======================
class Turno(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, related_name='turnos')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='turnos')
    fecha_hora = models.DateTimeField()

    # Estado del turno
    PENDIENTE = 'Pendiente'
    CONFIRMADO = 'Confirmado'
    CANCELADO = 'Cancelado'
    REALIZADO = 'Realizado'
    ESTADO_CHOICES = (
        (PENDIENTE, 'Pendiente'),
        (CONFIRMADO, 'Confirmado'),
        (CANCELADO, 'Cancelado'),
        (REALIZADO, 'Realizado'),
    )
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default=PENDIENTE)
    motivo = models.TextField(blank=True, null=True)

    # Auditoría
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='turnos_creados')
    modificado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='turnos_modificados')

    # Fechas automáticas
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['fecha_hora']
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"
        constraints = [
            models.UniqueConstraint(fields=['agenda', 'fecha_hora'], name='unique_turno_agenda_fecha')
        ]

    def __str__(self):
        return f"{self.id} ) {self.fecha_hora} : {self.paciente} | {self.agenda.profesional}"