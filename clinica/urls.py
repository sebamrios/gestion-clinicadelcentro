
from django.contrib import admin
from django.urls import path, include
from myApps.profesionales.views import home 

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('profesionales/', include('myApps.profesionales.urls')),
    path('alquileres/', include('myApps.alquileres.urls')),
    path('contacto/', include('myApps.contacto.urls')),
    path('usuarios/', include('myApps.usuarios.urls')),
    path('pacientes/', include('myApps.pacientes.urls')),
    path('secretarias/', include('myApps.secretarias.urls')),
    path('turnos/', include('myApps.turnos.urls')),
]