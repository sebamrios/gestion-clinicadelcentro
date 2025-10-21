from django.urls import path
from . import views

urlpatterns = [
    path('', views.alquileres_view, name='alquileres'),
]