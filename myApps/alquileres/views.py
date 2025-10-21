from django.shortcuts import render

# utilizando funciones para las vistas 
def alquileres_view(request):
    return render(request, 'alquileres/lista.html')