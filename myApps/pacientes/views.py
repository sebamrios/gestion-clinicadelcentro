from django.http import HttpResponse
from django.http import JsonResponse
from .models import Paciente
import json
from django.http import HttpResponse
from django.views import View
from .models import Paciente
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PacienteForm



def index(request):
    return HttpResponse("Bienvenido a la gestión de pacientes")

class AgregarPacienteAjax(View):
    def post(self, request, *args, **kwargs):
        print("POST recibido")  # <-- Ver si llega aquí
        print("Headers:", request.headers)
        print("POST data:", request.POST)

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            print("Es AJAX")
            apellido = request.POST.get("apellido")
            nombre   = request.POST.get("nombre")
            documento      = request.POST.get("documento")
            print(f"Datos recibidos -> Apellido: {apellido}, Nombre: {nombre}, Documento: {documento}")

            if apellido and nombre and documento:
                paciente = Paciente.objects.create(
                    apellido=apellido,
                    nombre=nombre,
                    documento=documento
                )
                print(f"Paciente creado con ID: {paciente.id}")
                return JsonResponse({
                    "success": True,
                    "id": paciente.id,
                    "nombre_completo": f"{paciente.apellido}, {paciente.nombre}"
                })
            else:
                print("Faltan datos")
                return JsonResponse({"success": False, "error": "Faltan datos"})
        else:
            print("No es AJAX")
            return JsonResponse({"success": False, "error": "Petición inválida"})

def buscar_paciente(request):
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        term = request.GET.get("term", "")
        pacientes = Paciente.objects.filter(apellido__icontains=term)[:10]  # límite de 10 resultados
        results = []
        for p in pacientes:
            results.append({
                "id": p.id,
                "label": f"{p.apellido}, {p.nombre} ({p.documento})",
                "value": f"{p.apellido}, {p.nombre}",
            })
        return JsonResponse(results, safe=False)
    return JsonResponse([], safe=False)

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/listar.html', {'pacientes': pacientes})

def agregar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/form_paciente.html', {'form': form, 'titulo': 'Agregar Paciente'})

def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'pacientes/form_paciente.html', {'form': form, 'titulo': 'Editar Paciente'})

def eliminar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('listar_pacientes')
    return render(request, 'pacientes/confirmar_eliminar.html', {'paciente': paciente})