from django.urls import path
from . import views
from .views import CrearEspecialidad
from .views import BuscarProfesional

urlpatterns = [
    path('', views.listar_profesionales, name='lista_profesionales'),
    path('crear/', views.crear_profesional, name='crear_profesional'),
    path('listar/', views.listar_profesionales, name='lista_profesionales'),
    path('filtrar/', views.filtrar_profesionales, name='filtrar_profesionales'),
    path('buscar/', BuscarProfesional.as_view(), name='buscar_profesional'),
    path('especialidades/crearEspecialidad/', CrearEspecialidad.as_view(), name='crear_especialidad'),
    path('editar/<int:profesional_id>/', views.editar_profesional, name='editar_profesional'),
    path('eliminar/<int:profesional_id>/', views.eliminar_profesional, name='eliminar_profesional'),
]
