from django.shortcuts import render, redirect, HttpResponse
from Usuarios.forms import *
from Usuarios.funciones import *

# Create your views here.


def registrarUsuario(request):

    if request.method == 'POST':
        formulario = FormularioRegistrarUsuario(data = request.POST)

        if not validarCorreo(request):

            if not validarNombre(request):

                insertarUsuarios(request)

                return redirect('Login')

            else:
                return redirect('/registrar/?errorNombre')
            
        else:
            return redirect('/registrar/?errorMail')

    else:

        formulario = FormularioRegistrarUsuario()

        return render(request, 'Registrar.html', {'form': formulario})


def login(request):

    if not validarSession(request): 
    
        if request.method == 'POST':

            formulario = FormularioLogin(data = request.POST)

            if validarCorreo(request):
                if validarPass(request):
                    nombre = request.POST['email']
                    request.session['nombre'] = nombre
                    return redirect('home/')
                else:
                    return redirect('/?errorPass')
            else:
                return redirect('/?errorMail')

        else:
            formulario = FormularioLogin()

            return render(request, 'Login.html', {'form': formulario})
    else:
        return redirect('/home/')
    
def logout(request):
    del request.session['nombre']
    return redirect('/home/')


def home(request):
    if validarSession(request):    
        nombre = request.session.get('nombre')
        return render(request, 'Session.html',{'name' : nombre})
    else:
        return redirect('Login')