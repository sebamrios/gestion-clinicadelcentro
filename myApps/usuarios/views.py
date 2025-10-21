
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegistroUsuarioForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm

# Create your views here.

#preguntar si es necesario crear 3 views.py separados para cada funcion?

def registrar(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            # loguea automáticamente al crear cuenta
            login(request, user)  
            print("Usuario se ha registrado correctamente")
            messages.success(request, "Registro exitoso")
            # y direccionar a la pagina principal en caso de exito
            return redirect('completar_perfil')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def loguear(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Usuario se ha logueado correctamente")
            return redirect('home')
        else:
            #mesaje de error
            print("Usuario ha ingresado datos incorrectos")
            messages.error(request, "Usuario o contraseña incorrectos")
    return render(request, 'usuarios/login.html')

def desloguear(request):
    logout(request)
    print("Usuario ha desloguedo correctamente")
    return redirect('home')

#cuando se crea un perfil, se conecta por signal a completar el perfil de usuario
@login_required
def completar_perfil(request):
    usuario = request.user.usuario  # accedemos al perfil asociado
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('home')  #se redirije a home despues de guardar
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'usuarios/perfil.html', {'form': form})
