from django.shortcuts import render, redirect, get_object_or_404
from .models import Profesional, Especialidad
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import View
import json


def home(request):
    especialidades = Especialidad.objects.all()
    for especialidad in especialidades:
        especialidad.profesionales_activos = especialidad.profesionales.filter(estado='Activo')
    return render(request, 'clinica/home.html', {
        'especialidades': especialidades
    })

def crear_profesional(request):
    if request.method == 'POST':
        nombre_completo = request.POST['profesional']
        patologia = request.POST['patologia']
        poblacion = request.POST['poblacion']
        especialidad_id = request.POST['especialidad']
        obras_sociales = request.POST['obras_sociales']
        contacto = request.POST['contacto']
        horarios = request.POST['horarios']

        especialidad = Especialidad.objects.get(id=especialidad_id)
        Profesional.objects.create(
            nombre_completo=nombre_completo,
            patologia=patologia,
            poblacion=poblacion,
            especialidad=especialidad,
            obras_sociales=obras_sociales,
            contacto=contacto,
            horarios=horarios
        )
        return redirect('lista_profesionales')

    especialidades = Especialidad.objects.all()
    return render(request, 'profesionales/crear.html', {'especialidades': especialidades})

def editar_profesional(request, profesional_id):
    profesional = get_object_or_404(Profesional, id=profesional_id)

    if request.method == 'POST':
        profesional.nombre_completo = request.POST['nombre_completo']
        profesional.especialidad = Especialidad.objects.get(id=request.POST['especialidad'])
        profesional.estado = request.POST['estado']
        profesional.patologia = request.POST['patologia']
        profesional.poblacion = request.POST['poblacion']
        profesional.obras_sociales = request.POST['obras_sociales']
        profesional.contacto = request.POST['contacto']
        profesional.horarios = request.POST['horarios']
        profesional.save()
        return redirect('lista_profesionales')

    especialidades = Especialidad.objects.all()
    return render(
        request,
        'profesionales/editar.html',
        {
            'profesional': profesional,
            'especialidades': especialidades,
            'estados': Profesional.ESTADO_PROFESIONAL,
        }
    )

def eliminar_profesional(request, profesional_id):
    profesional = get_object_or_404(Profesional, id=profesional_id)
    profesional.delete()
    return redirect('lista_profesionales')

def listar_profesionales(request):
    especialidades = Especialidad.objects.all()
    for especialidad in especialidades:
        profesionales_activos = especialidad.profesionales.filter(estado='Activo')
        especialidad.profesionales_activos = profesionales_activos
    return render(request, 'profesionales/lista.html', {
        'especialidades': especialidades,
    })

def filtrar_profesionales(request):
    profesionales = Profesional.objects.all()
    especialidades = Especialidad.objects.all()
    context = {
        'profesionales': profesionales,
        'especialidades': especialidades,
    }
    return render(request, 'profesionales/filtrar.html', context)

class CrearEspecialidad(CreateView):
    model = Especialidad
    template_name = 'profesionales/crearEspecialidades.html'
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('lista_profesionales')

class BuscarProfesional(View):
    def get(self, request):
        query = request.GET.get('term', '')
        print(query)

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
       # if request.is_ajax:
            # Si la solicitud es AJAX, se procesa la búsqueda.
            
            profesionales_query = Profesional.objects.filter(nombre_completo__icontains=query)

            result = []
            for profesional in profesionales_query:
                data = {}
                data['label'] = f"{profesional.nombre_completo} ({profesional.especialidad.nombre})"
                data['value'] = profesional.nombre_completo
                data['contacto'] = profesional.contacto
                data['obras_sociales'] = profesional.obras_sociales
                data['horarios'] = profesional.horarios
                data['poblacion'] = profesional.poblacion
                result.append(data)
            
            data_json = json.dumps(result)
            mimetype = "application/json"
            return HttpResponse(data_json, mimetype)
        
        else:
            # Si no es una solicitud AJAX, solo se renderiza la plantilla.
            return render(request, 'profesionales/buscar.html')
