from django.db import models
from django.conf import settings

# Create your models here.
from django.db import models
from django.conf import settings

class Secretaria(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="secretaria"
    )
    documento = models.CharField(max_length=8, blank=True, null=True)
    fecha_nac = models.DateField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return f"{self.usuario.get_full_name()}"

#---------------------------------------------------------------------------

class Licencia(models.Model):
    TIPO_CHOICES = [
        ("VAC", "Vacaciones"),
        ("MED", "Licencia Médica"),
        ("PER", "Permiso Especial"),
        ("OTR", "Otra"),
    ]

    secretaria = models.ForeignKey(
        'Secretaria',
        on_delete=models.CASCADE,
        related_name='licencias'
    )
    tipo = models.CharField(max_length=3, choices=TIPO_CHOICES, default="VAC")
    periodo = models.PositiveIntegerField(help_text="Año al que corresponde la licencia")
    dias_totales = models.PositiveIntegerField(default=0)
    fecha_inicio_licencia = models.DateField(blank=True, null=True)
    fecha_fin_licencia = models.DateField(blank=True, null=True)
    suplente = models.ForeignKey(
        'Secretaria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='suplencias'
    )

    @property
    def dias_tomados(self):
        return sum(tramo.dias_tomados for tramo in self.tramos.all())

    @property
    def dias_pendientes(self):
        return max(self.dias_totales - self.dias_tomados, 0)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.secretaria} ({self.periodo})"

#------------------------------------------------------------------------------------------------------------------
class TramoLicencia(models.Model):
    licencia = models.ForeignKey(
        Licencia,
        on_delete=models.CASCADE,
        related_name='tramos'
    )
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    dias_tomados = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Ingrese la cantidad real de días computables (excluyendo fines de semana y feriados)"
    )

    def save(self, *args, **kwargs):
        if self.dias_tomados is None:
            # Solo calcula automáticamente si el usuario no ingresó valor
            self.dias_tomados = (self.fecha_fin - self.fecha_inicio).days + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.licencia.secretaria} | {self.licencia.tipo} | {self.dias_tomados} días"