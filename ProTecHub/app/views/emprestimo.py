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

from app.models import Usuario, Equipamento, Emprestimo
from app.forms import EmprestimoForm
from django.contrib.auth.decorators import login_required
from .base import home, logar
from app.utils import obter_data_resumida

from app.utils.enums import StatusEmprestimo

@login_required()
def obter_emprestimos(request: WSGIRequest) -> HttpResponse:
    user = request.user

    # O Usuário está autenticado?
    if not user.is_authenticated:
        messages.error(request, 'Você não está logado!')
        return redirect(logar)

    # Verifica se o 'ROLE' do 'Usuário' não é 'Admin' ou 'Supervisor' ou 'Colaborador'
    if not user.groups.filter(name__in=['Admin', 'Supervisor', 'Colaborador']).exists():
        messages.warning(request, 'Você não possui permissão!')
        return redirect(home)   

    query = request.GET.get('search')
    if query:
        emprestimos: list[Emprestimo] = Emprestimo.objects.filter(status__icontains=query)
    else:
        emprestimos: list[Emprestimo] = Emprestimo.objects.all()

    user_groups = request.user.groups.values_list('name', flat=True)
    foto = Usuario.objects.filter(id=request.user.pk).values_list('foto', flat=True).first()
    status_disponiveis = [
        StatusEmprestimo.EMPRESTADO.label,
        StatusEmprestimo.EM_USO.label,
        StatusEmprestimo.FORNECIDO.label
    ]

    # Formata a 'data_emprestimo' e 'data_devolucao_prevista' para exibição
    for emprestimo in emprestimos:
        emprestimo.data_emprestimo = obter_data_resumida(emprestimo.data_emprestimo)
        emprestimo.data_devolucao_prevista = obter_data_resumida(emprestimo.data_devolucao_prevista)

    context = {
        'user_groups': user_groups,
        'emprestimos': emprestimos,
        'status_disponiveis': status_disponiveis,
        'foto': foto,
        'MEDIA_URL': settings.MEDIA_URL
    }

    return render(request, 'pages/interno/emprestimo/listar_emprestimos.html', context)


@login_required()
def criar_emprestimo(request: WSGIRequest) -> HttpResponse:
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
        permitir_emprestimo = True

        id_equipamento: int = request.POST.get('equipamento')
        equipamento = Equipamento.objects.get(id=id_equipamento)

        quantidade_emprestimo = int(request.POST.get('quantidade')) 

        if equipamento.quantidade_disponivel <= 0 or quantidade_emprestimo > equipamento.quantidade_disponivel:
            permitir_emprestimo = False
            messages.info(request, f"O Equipamento {equipamento.nome} não possui estoque suficiente!")
        elif quantidade_emprestimo <= 0:
            permitir_emprestimo = False
            messages.info(request, f"A quantidade deve ser maior que 0!")

        form = EmprestimoForm(request.POST)

        if permitir_emprestimo and form.is_valid():
            form.save()
            messages.success(request, 'Empréstimo criado com sucesso!')
            return redirect(obter_emprestimos) 
    else:
        form = EmprestimoForm()

    user_groups = request.user.groups.values_list('name', flat=True)
    foto = Usuario.objects.filter(id=request.user.pk).values_list('foto', flat=True).first()

    context = {
        'user_groups': user_groups,
        'form': form,
        'foto': foto,
        'MEDIA_URL': settings.MEDIA_URL
    }

    return render(request, 'pages/interno/emprestimo/criar_emprestimo.html', context)


@login_required()
def deletar_emprestimo(request: WSGIRequest, id: int) -> HttpResponse:
    user = request.user

    # O Usuário está autenticado?
    if not user.is_authenticated:
        messages.error(request, 'Você não está logado!')
        return redirect(logar)

    # Verifica se o 'ROLE' do 'Usuário' não é 'Admin' ou 'Supervisor' ou 'Colaborador'
    if not user.groups.filter(name__in=['Admin', 'Supervisor', 'Colaborador']).exists():
        messages.warning(request, 'Você não possui permissão!')
        return redirect(home)    

    emprestimo = get_object_or_404(Emprestimo, id=id)
    emprestimo.delete()
    messages.success(request, 'Empréstimo deletado com sucesso!')

    return redirect(obter_emprestimos)


@login_required()
def atualizar_emprestimo(request: WSGIRequest, id: int) -> HttpResponse:
    user = request.user

    # O Usuário está autenticado?
    if not user.is_authenticated:
        messages.error(request, 'Você não está logado!')
        return redirect(logar)

    # Verifica se o 'ROLE' do 'Usuário' não é 'Admin' ou 'Supervisor' ou 'Colaborador'
    if not user.groups.filter(name__in=['Admin', 'Supervisor', 'Colaborador']).exists():
        messages.warning(request, 'Você não possui permissão!')
        return redirect(home)

    emprestimo = get_object_or_404(Emprestimo, id=id) 
    
    if request.method == 'POST':
        permitir_emprestimo: bool = True

        id_equipamento: int = request.POST.get('equipamento')
        equipamento = Equipamento.objects.get(id=id_equipamento)

        quantidade_emprestimo = int(request.POST.get('quantidade', 1)) 
        quantidade_disponivel =  equipamento.quantidade_disponivel + emprestimo.quantidade

        if quantidade_disponivel <= 0 or quantidade_emprestimo > quantidade_disponivel:
            permitir_emprestimo = False
            messages.info(request, f"O Equipamento {equipamento.nome} não possui estoque suficiente!")
        elif quantidade_emprestimo <= 0:
            permitir_emprestimo = False
            messages.info(request, f"A quantidade deve ser maior que 0!")

        form = EmprestimoForm(request.POST, instance=emprestimo)
        if permitir_emprestimo and form.is_valid():
            form.save()
            messages.success(request, 'Empréstimo atualizado com sucesso!')
            return redirect(obter_emprestimos)
    else:
        form = EmprestimoForm(instance=emprestimo)

    user_groups = request.user.groups.values_list('name', flat=True)
    foto = Usuario.objects.filter(id=request.user.pk).values_list('foto', flat=True).first()

    context = {
        'user_groups': user_groups,
        'form': form,
        'emprestimo': emprestimo,
        'foto': foto,
        'MEDIA_URL': settings.MEDIA_URL
    }

    return render(request, 'pages/interno/emprestimo/atualizar_emprestimo.html', context)
