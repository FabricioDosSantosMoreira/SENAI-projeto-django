from datetime import datetime
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest

from app.models import Usuario, Equipamento
from app.forms import EquipamentoForm
from django.contrib.auth.decorators import login_required
import pytz
from .base import home, logar
from app.utils import obter_data_resumida


@login_required()
def obter_equipamentos(request: WSGIRequest) -> HttpResponse:
    user = request.user

    # O Usuário está autenticado?
    if not user.is_authenticated:
        messages.error(request, 'Você não está logado!')
        return redirect(logar)

    # Verifica se o 'ROLE' do 'Usuário' não é 'Admin' ou 'Supervisor'
    if not user.groups.filter(name__in=['Admin', 'Supervisor']).exists():
        messages.warning(request, 'Você não possui permissão!')
        return redirect(home)   

    query = request.GET.get('search')
    if query:
        equipamentos: list[Equipamento] = Equipamento.objects.filter(nome__icontains=query)
    else:
        equipamentos: list[Equipamento] = Equipamento.objects.all()

    user_groups = request.user.groups.values_list('name', flat=True)
    foto = Usuario.objects.filter(id=request.user.pk).values_list('foto', flat=True).first()

    # Formata a 'validade' para exibição
    for equipamento in equipamentos:
        equipamento.validade = obter_data_resumida(equipamento.validade)

    context = {
        'user_groups': user_groups,
        'equipamentos': equipamentos,
        'foto': foto,
        'MEDIA_URL': settings.MEDIA_URL
    }

    return render(request, 'pages/interno/equipamento/listar_equipamentos.html', context)


@login_required()
def criar_equipamento(request: WSGIRequest) -> HttpResponse:
    user = request.user

    # O Usuário está autenticado?
    if not user.is_authenticated:
        messages.error(request, 'Você não está logado!')
        return redirect(logar)

    # Verifica se o 'ROLE' do 'Usuário' não é 'Admin' ou 'Supervisor'
    if not user.groups.filter(name__in=['Admin', 'Supervisor']).exists():
        messages.warning(request, 'Você não possui permissão!')
        return redirect(home)

    if request.method == 'POST':
        form = EquipamentoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento criado com sucesso!')
            return redirect(obter_equipamentos)
    else:
        form = EquipamentoForm()

    user_groups = request.user.groups.values_list('name', flat=True)
    foto = Usuario.objects.filter(id=request.user.pk).values_list('foto', flat=True).first()

    context = {
        'user_groups': user_groups,
        'form': form,
        'foto': foto,
        'MEDIA_URL': settings.MEDIA_URL
    }

    return render(request, 'pages/interno/equipamento/criar_equipamento.html', context)


@login_required()
def deletar_equipamento(request: WSGIRequest, id: int) -> HttpResponse:
    user = request.user

    # O Usuário está autenticado?
    if not user.is_authenticated:
        messages.error(request, 'Você não está logado!')
        return redirect(logar)

    # Verifica se o 'ROLE' do 'Usuário' não é 'Admin' ou 'Supervisor'
    if not user.groups.filter(name__in=['Admin', 'Supervisor']).exists():
        messages.warning(request, 'Você não possui permissão!')
        return redirect(home)    

    equipamento = get_object_or_404(Equipamento, id=id)
    equipamento.delete()
    messages.success(request, 'Equipamento deletado com sucesso!')

    return redirect(obter_equipamentos)


@login_required()
def atualizar_equipamento(request: WSGIRequest, id: int) -> HttpResponse:
    user = request.user

    # O Usuário está autenticado?
    if not user.is_authenticated:
        messages.error(request, 'Você não está logado!')
        return redirect(logar)

    # Verifica se o 'ROLE' do 'Usuário' não é 'Admin' ou 'Supervisor'
    if not user.groups.filter(name__in=['Admin', 'Supervisor']).exists():
        messages.warning(request, 'Você não possui permissão!')
        return redirect(home)

    equipamento: Equipamento = get_object_or_404(Equipamento, id=id) 

    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)

        if form.is_valid():
            form.save()  
            messages.success(request, 'Equipamento atualizado com sucesso!')
            return redirect(obter_equipamentos)
    else:
        form = EquipamentoForm(instance=equipamento)

    user_groups = request.user.groups.values_list('name', flat=True)
    foto = Usuario.objects.filter(id=request.user.pk).values_list('foto', flat=True).first()

    context = {
        'user_groups': user_groups,
        'form': form,
        'equipamento': equipamento,
        'foto': foto,
        'MEDIA_URL': settings.MEDIA_URL
    }

    return render(request, 'pages/interno/equipamento/atualizar_equipamento.html', context)
