from django.urls import path
from myApps.contacto import views
from myApps.contacto.views import Contacto, MensajeEnviado

urlpatterns = [
    path("", Contacto.as_view(), name="contacto"),
    path("mensaje_enviado", MensajeEnviado.as_view(), name="mensaje_enviado"),
]
