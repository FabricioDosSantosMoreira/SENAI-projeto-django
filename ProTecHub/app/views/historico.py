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

from app.models import Usuario, Historico, Emprestimo
from app.forms import HistoricoForm
from django.contrib.auth.decorators import login_required
from .base import home, logar
from app.utils import obter_data_resumida
from app.utils.enums import StatusEmprestimo


@login_required
def obter_historico(request: WSGIRequest) -> HttpResponse:
    user = request.user

    # O Usuário está autenticado?
    if not user.is_authenticated:
        messages.error(request, 'Você não está logado!')
        return redirect(logar)

    # Verifica se o 'ROLE' do 'Usuário' não é 'Admin' ou 'Supervisor'
    if not user.groups.filter(name__in=['Admin', 'Supervisor']).exists():
        messages.warning(request, 'Você não possui permissão!')
        return redirect(home)   

    status_query = request.GET.get('search-by-status')
    name_query = request.GET.get('search-by-name')

    # Construindo um dicionário de argumentos para o filtro
    filter_args = {}
    if status_query:
        filter_args['status'] = status_query
    if name_query:
        filter_args['nome_usuario__contains'] = name_query

    # Aplicando o filtro dinâmico com base nos argumentos fornecidos
    itens_historico = Historico.objects.filter(**filter_args)

    status_disponiveis = [
        StatusEmprestimo.DEVOLVIDO.label,
        StatusEmprestimo.DANIFICADO.label,
        StatusEmprestimo.PERDIDO.label
    ]
    user_groups = request.user.groups.values_list('name', flat=True)
    foto = Usuario.objects.filter(id=request.user.pk).values_list('foto', flat=True).first()

    # Formata a 'validade' para exibição
    for item in itens_historico:
        item.data_emprestimo = obter_data_resumida(item.data_emprestimo)

        if item.data_devolucao_efetiva:
            item.data_devolucao_efetiva = obter_data_resumida(item.data_devolucao_efetiva)
        else:
            item.data_devolucao_efetiva = 'NULO'

    context = {
        'user_groups': user_groups,
        'itens_historico': itens_historico,
        'status_disponiveis': status_disponiveis,
        'foto': foto,
        'MEDIA_URL': settings.MEDIA_URL
    }

    return render(request, 'pages/interno/historico/listar_historico.html', context)


@login_required()
def arquivar_emprestimo_no_historico(request: WSGIRequest, id_emprestimo: int) -> HttpResponse:
    user = request.user

    # O Usuário está autenticado?
    if not user.is_authenticated:
        messages.error(request, 'Você não está logado!')
        return redirect(logar)

    # Verifica se o 'ROLE' do 'Usuário' não é 'Admin' ou 'Supervisor'
    if not user.groups.filter(name__in=['Admin', 'Supervisor']).exists():
        messages.warning(request, 'Você não possui permissão!')
        return redirect(home)
    
    emprestimo = get_object_or_404(Emprestimo, id=id_emprestimo)
    nome_usuario = emprestimo.usuario.nome
    nome_equipamento = emprestimo.equipamento.nome
    data_emprestimo =  emprestimo.data_emprestimo
    quantidade =  emprestimo.quantidade

    historico = Historico(
        nome_usuario=nome_usuario,
        nome_equipamento=nome_equipamento,
        data_emprestimo=data_emprestimo,
        quantidade=quantidade
    )

    if request.method == 'POST':
        form = HistoricoForm(request.POST)

        if form.is_valid():
            historico = form.save(commit=False)
            historico.nome_usuario = nome_usuario
            historico.nome_equipamento = nome_equipamento
            historico.data_emprestimo = data_emprestimo
            historico.quantidade = quantidade
            historico.save()

            # Deleta o empréstimo após arquivar no histórico
            emprestimo.delete()

            messages.success(request, 'Empréstimo arquivado com sucesso!')
            return redirect(obter_historico)
    else:
        form = HistoricoForm(instance=historico)

    user_groups = request.user.groups.values_list('name', flat=True)
    foto = Usuario.objects.filter(id=request.user.pk).values_list('foto', flat=True).first()

    context = {
        'user_groups': user_groups,
        'form': form,
        'emprestimo': emprestimo,
        'foto': foto,
        'MEDIA_URL': settings.MEDIA_URL
    }

    return render(request, 'pages/interno/historico/criar_historico.html', context)


@login_required()
def deletar_item_historico(request: WSGIRequest, id: int) -> HttpResponse:
    user = request.user

    # O Usuário está autenticado?
    if not user.is_authenticated:
        messages.error(request, 'Você não está logado!')
        return redirect(logar)

    # Verifica se o 'ROLE' do 'Usuário' não é 'Admin' ou 'Supervisor'
    if not user.groups.filter(name__in=['Admin', 'Supervisor']).exists():
        messages.warning(request, 'Você não possui permissão!')
        return redirect(home)    

    item_historico = get_object_or_404(Historico, id=id)
    item_historico.delete()
    messages.success(request, 'Item deletado com sucesso!')

    return redirect(obter_historico)


@login_required()
def atualizar_item_historico(request: WSGIRequest, id: int) -> HttpResponse:
    user = request.user

    # O Usuário está autenticado?
    if not user.is_authenticated:
        messages.error(request, 'Você não está logado!')
        return redirect(logar)

    # Verifica se o 'ROLE' do 'Usuário' não é 'Admin' ou 'Supervisor'
    if not user.groups.filter(name__in=['Admin', 'Supervisor']).exists():
        messages.warning(request, 'Você não possui permissão!')
        return redirect(home)

    item_historico = get_object_or_404(Historico, id=id) 

    if request.method == 'POST':
        form = HistoricoForm(request.POST, instance=item_historico)

        if form.is_valid():
            # NOTE: NÃO ME REMOVA
            item_historico = get_object_or_404(Historico, id=id) 

            historico = form.save(commit=False)
            historico.nome_usuario = item_historico.nome_usuario
            historico.nome_equipamento = item_historico.nome_equipamento
            historico.data_emprestimo = item_historico.data_emprestimo
            historico.quantidade = item_historico.quantidade
            historico.save()

            messages.success(request, 'Item atualizado com sucesso!')
            return redirect(obter_historico)
    else:
        form = HistoricoForm(instance=item_historico)

    user_groups = request.user.groups.values_list('name', flat=True)
    foto = Usuario.objects.filter(id=request.user.pk).values_list('foto', flat=True).first()

    context = {
        'user_groups': user_groups,
        'form': form,
        'item_historico': item_historico,
        'foto': foto,
        'MEDIA_URL': settings.MEDIA_URL
    }

    return render(request, 'pages/interno/historico/atualizar_historico.html', context)
