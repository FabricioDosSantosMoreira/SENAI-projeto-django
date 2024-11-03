from datetime import datetime
from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.conf import settings

import pytz
from .base import home, logar
from app.models import Usuario
from app.forms import UsuarioForm
from app.utils.enums import TipoUsuario
from django.contrib.auth.decorators import login_required

from app.utils import obter_data_resumida

@login_required()
def obter_usuarios(request: WSGIRequest) -> HttpResponse: 
    user = request.user

    # O Usuário está autenticado?
    if not user.is_authenticated:
        messages.error(request, 'Você não está logado!')
        return redirect(logar)

    # Verifica se o 'ROLE' do 'Usuário' não é 'Admin'
    if not user.groups.filter(name='Admin').exists():
        messages.warning(request, 'Você não possui permissão!')
        return redirect(home)    
    
    query = request.GET.get('search')
    if query:
        usuarios: List[Usuario] = Usuario.objects.filter(nome__icontains=query)
    else:
        usuarios: List[Usuario] = Usuario.objects.all()

    user_groups = request.user.groups.values_list('name', flat=True)
    foto = Usuario.objects.filter(id=request.user.pk).values_list('foto', flat=True).first()

    # Formata a 'data_admissao' para exibição
    for usuario in usuarios:
        usuario.data_admissao = obter_data_resumida(usuario.data_admissao)

    context = {
        'user_groups': user_groups,
        'usuarios': usuarios,
        'foto': foto,
        'MEDIA_URL': settings.MEDIA_URL
    }
        
    return render(request, 'pages/interno/usuario/listar_usuarios.html', context)


@login_required()
def criar_usuario(request: WSGIRequest) -> HttpResponse:
    user = request.user

    # O Usuário está autenticado?
    if not user.is_authenticated:
        messages.error(request, 'Você não está logado!')
        return redirect(logar)

    # Verifica se o 'ROLE' do 'Usuário' não é 'Admin'
    if not user.groups.filter(name='Admin').exists():
        messages.warning(request, 'Você não possui permissão!')
        return redirect(home)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect(obter_usuarios)
    else:
        form = UsuarioForm()

    user_groups = request.user.groups.values_list('name', flat=True)
    foto = Usuario.objects.filter(id=request.user.pk).values_list('foto', flat=True).first()

    context = {
        'user_groups': user_groups,
        'form': form,
        'foto': foto,
        'MEDIA_URL': settings.MEDIA_URL
    }
    
    return render(request, 'pages/interno/usuario/criar_usuario.html', context)


@login_required()
def deletar_usuario(request: WSGIRequest, id: int) -> HttpResponse:
    user = request.user

    # O Usuário está autenticado?
    if not user.is_authenticated:
        messages.error(request, 'Você não está logado!')
        return redirect(logar)

    # Verifica se o 'ROLE' do 'Usuário' não é 'Admin'
    if not user.groups.filter(name='Admin').exists():
        messages.warning(request, 'Você não possui permissão!')
        return redirect(home)    

    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    messages.success(request, 'Usuário deletado com sucesso!')

    return redirect(obter_usuarios)


@login_required()
def atualizar_usuario(request: WSGIRequest, id: int) -> HttpResponse:
    user = request.user

    # O Usuário está autenticado?
    if not user.is_authenticated:
        messages.error(request, 'Você não está logado!')
        return redirect(login)

    # Verifica se o 'ROLE' do 'Usuário' não é 'Admin'
    if not user.groups.filter(name='Admin').exists():
        messages.warning(request, 'Você não possui permissão!')
        return redirect(logar)
    
    usuario = get_object_or_404(Usuario, id=id) 

    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)

        if form.is_valid():
            form.save()  
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect(obter_usuarios)
    else:
        form = UsuarioForm(instance=usuario)

    user_groups = request.user.groups.values_list('name', flat=True)
    
    context = {
        'user_groups': user_groups,
        'form': form,
        'usuario': usuario,
        'foto': usuario.foto,
        'MEDIA_URL': settings.MEDIA_URL
    }
    
    return render(request, 'pages/interno/usuario/atualizar_usuario.html', context)
