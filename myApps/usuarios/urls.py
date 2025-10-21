from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registrar, name='registro'),
    path('login/', views.loguear, name='login'),
    path('logout/', views.desloguear, name='logout'),
    path('perfil/', views.completar_perfil, name='completar_perfil'),
]