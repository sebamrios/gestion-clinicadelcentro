from django.urls import path
from . import views

urlpatterns = [
    path("agendas/", views.elegir_agenda, name="elegir_agenda"),
    path("agendas/<int:agenda_id>/", views.ver_agenda, name="ver_agenda"),
    path("agendas/<int:agenda_id>/json/", views.turnos_json, name="turnos_json"),
    path("agendas/<int:agenda_id>/calendario/", views.agenda_calendario, name="agenda_calendario"), 
    path("turno/<int:turno_id>/editar/", views.editar_turno, name="editar_turno"),
]