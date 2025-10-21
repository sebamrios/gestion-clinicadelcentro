from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.nombre


class Profesional(models.Model):
    
    Activo = 'Activo'
    Inactivo = 'Inactivo'

    ESTADO_PROFESIONAL = (
        (Activo, 'Activo'),
        (Inactivo, 'Inactivo'),
    )

    nombre_completo = models.CharField(max_length=100)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, related_name='profesionales')
    estado = models.CharField(max_length=10, choices=ESTADO_PROFESIONAL, default='Activo')
    patologia = models.CharField(max_length=100)
    poblacion = models.CharField(max_length=100)
    obras_sociales = models.CharField(max_length=200)
    contacto = models.CharField(max_length=50)
    horarios = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"

    def __str__(self):
        return self.nombre_completo