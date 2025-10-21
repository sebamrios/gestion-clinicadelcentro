from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Prefetch
from django.utils.timezone import localdate
from django.contrib import messages
from collections import defaultdict
from datetime import timedelta
from myApps.pacientes.models import Paciente
from .models import Agenda, Turno


# ======================
# Vistas básicas
# ======================

def index(request):
    return HttpResponse("Bienvenido a la gestión de turnos")


def elegir_agenda(request):
    agendas = Agenda.objects.select_related("profesional").all()
    return render(request, "turnos/elegir_agenda.html", {"agendas": agendas})


def ver_agenda(request, agenda_id):
    agenda = get_object_or_404(Agenda, id=agenda_id)

    turnos = agenda.turnos.select_related("paciente").order_by("-fecha_hora")

    # Agrupar turnos por fecha (vista clásica)
    turnos_por_dia = defaultdict(list)
    for turno in turnos:
        dia = localdate(turno.fecha_hora)  # yyyy-mm-dd
        turnos_por_dia[dia].append(turno)

    if request.method == "POST":
        paciente_id = request.POST.get("paciente_id")
        fecha_hora = request.POST.get("fecha_hora")

        if paciente_id and fecha_hora:
            paciente = get_object_or_404(Paciente, id=paciente_id)

            if Turno.objects.filter(agenda=agenda, fecha_hora=fecha_hora).exists():
                messages.error(request, "Ya existe un turno en ese horario para esta agenda.")
            else:
                Turno.objects.create(
                    agenda=agenda,
                    paciente=paciente,
                    fecha_hora=fecha_hora,
                    creado_por=request.user,
                )
                messages.success(request, "Turno creado correctamente.")
                return redirect("ver_agenda", agenda_id=agenda.id)

    pacientes = Paciente.objects.all()

    return render(
        request,
        "turnos/ver_agenda.html",
        {
            "agenda": agenda,
            "turnos_por_dia": dict(turnos_por_dia),
            "pacientes": pacientes,
        },
    )


def editar_turno(request, turno_id):
    turno = get_object_or_404(Turno, id=turno_id)

    if request.method == 'POST':
        turno.fecha_hora = request.POST['fecha_hora']
        turno.estado = request.POST['estado']
        turno.motivo = request.POST['motivo']
        turno.save()
        messages.success(request, "Turno actualizado correctamente")
        return redirect('ver_agenda', turno.agenda.id)

    return render(request, 'turnos/editar_turno.html', {
        'turno': turno,
        'estados': Turno.ESTADO_CHOICES,
    })


# ======================
# Vistas para FullCalendar
# ======================
def calendario_profesional(request, agenda_id):
    """
    Renderiza el calendario gráfico (FullCalendar) de un profesional
    """
    agenda = get_object_or_404(Agenda, id=agenda_id)
    return render(request, "turnos/calendario.html", {"agenda": agenda})

def turnos_json(request, agenda_id):
    """
    Devuelve los turnos de una agenda en formato JSON para FullCalendar
    """
    agenda = get_object_or_404(Agenda, id=agenda_id)
    turnos = agenda.turnos.select_related("paciente")

    eventos = []
    for t in turnos:
        eventos.append({
            "id": t.id,
            "title": f"{t.paciente.apellido}-{t.paciente.documento} ({t.estado})",
            "start": t.fecha_hora.isoformat(),
            "end": (t.fecha_hora + timedelta(minutes=30)).isoformat(),  
            "color": (
                "#28a745" if t.estado == Turno.CONFIRMADO
                else "#dc3545" if t.estado == Turno.CANCELADO
                else "#ffc107" if t.estado == Turno.PENDIENTE
                else "#17a2b8"
            ),
        })
    return JsonResponse(eventos, safe=False)

def agenda_calendario(request, agenda_id):
    agenda = get_object_or_404(Agenda, id=agenda_id)
    return render(request, "turnos/calendario.html", {"agenda": agenda})