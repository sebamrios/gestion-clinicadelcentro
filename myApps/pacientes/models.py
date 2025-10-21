from django.db import models
from django.conf import settings


class Paciente(models.Model):
    nombre = models.CharField(max_length=100, default="Sin Nombre")
    apellido = models.CharField(max_length=100, default="Sin Apellido")
    documento = models.CharField(max_length=10, unique=True)
    fecha_nac = models.DateField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    obra_social = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return f"{self.apellido} ({self.documento})"