from django.db import models
from datetime import datetime
from django.utils.html import format_html


class Consulta(models.Model):

    CONTESTADA = 'Contestada'
    NOCONTESTADA = 'Sin Contestar'
    ENPROCESO = 'En_Proceso'

    ESTADO = (
        (CONTESTADA, 'Contestada'),
        (NOCONTESTADA, 'Sin Contestar'),
        (ENPROCESO, 'En Proceso'),
    )
 
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=False, null=True) 
    mail = models.EmailField(max_length=50, blank=True, null=True)
    estado_respuesta = models.CharField(max_length=15, blank=True, choices=ESTADO, default=NOCONTESTADA)
    telefono = models.CharField(max_length=90, blank=True, null=True)
    fecha = models.DateField(default=datetime.now, blank=True, editable=True)

    def __str__(self):

        return self.nombre
    
    def estado_de_respuesta(self):
        if self.estado_respuesta == 'Contestada':
            return format_html('<span style="background-color:#0a0; color: #fff; padding:5px;">{}</span>', self.estado_respuesta, )
        elif self.estado_respuesta == 'Sin Contestar':
            return format_html('<span style="background-color:#a00; color: #fff; padding:5px;"">{}</span>', self.estado_respuesta, )
        elif self.estado_respuesta == 'En_Proceso':
            return format_html('<span style="background-color:#F0B203; color: #000; padding:5px;"">{}</span>', self.estado_respuesta, )


class Respuesta(models.Model):
    consulta  = models.ForeignKey(Consulta, blank=False, null=True, on_delete=models.CASCADE)
    respuesta = models.TextField()
    fecha     = models.DateField(default=datetime.now, blank=True, editable=False)

    def create_mensaje(self):
        consula_cambio_estado = Consulta.objects.get(id=self.consulta.id)
        consula_cambio_estado.estado_respuesta = "Contestada"
        consula_cambio_estado.save()

        #envio de mail

    def save(self, *args, **kwargs):
        self.create_mensaje()
        force_update = False
        if self.id:
            force_update = True
        super(Respuesta, self).save(force_update=force_update)
