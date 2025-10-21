from django.urls import path
from .views import AgregarPacienteAjax, buscar_paciente
from . import views

urlpatterns = [
    path('', views.lista_pacientes, name='listar_pacientes'),
    path('agregar/', views.agregar_paciente, name='agregar_paciente'),
    path('editar/<int:pk>/', views.editar_paciente, name='editar_paciente'),
    path('eliminar/<int:pk>/', views.eliminar_paciente, name='eliminar_paciente'),
    path("agregar-paciente-ajax/", AgregarPacienteAjax.as_view(), name="agregar_paciente_ajax"),
    path("buscar-paciente/", buscar_paciente, name="buscar_paciente"),  
]