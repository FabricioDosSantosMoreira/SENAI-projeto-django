from typing import Any, Dict

from app.forms import UsuarioForm
from app.models import Usuario

from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

def home(request: WSGIRequest) -> HttpResponse:
    return render(request, 'pages/home.html', status=200)


def cadastrar(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            messages.success(request, 'Usuário cadastrado com sucesso!')
            form.save()
            
            #return redirect(logar)
            form = UsuarioForm()
    else:
        form = UsuarioForm()

    context: Dict[str, Any] = {
        'form': form
    }

    return render(request, 'pages/cadastro.html', context)


def logar(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        _email: str = request.POST.get('email')
        _senha: str = request.POST.get('senha') 

        try:
            usuario = Usuario.objects.get(email=_email) 

            if usuario.validar_senha(_senha):
                login(request, usuario)
                messages.success(request, 'Log-in realizado com sucesso!')
        
                #return redirect(home)   
                return render(request, 'pages/login.html')
            else:
                messages.warning(request, 'E-mail ou Senha inválidos!')
                
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuário inexistente!')
    
    return render(request, 'pages/login.html')


def deslogar(request: WSGIRequest) -> HttpResponse:
    logout(request)
    messages.success(request, 'Log-out realizado com sucesso!')

    #return redirect(home)
    return render(request, 'pages/login.html')
