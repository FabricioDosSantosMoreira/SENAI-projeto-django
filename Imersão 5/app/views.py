from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from django.core.handlers.wsgi import WSGIRequest

from app.models import Usuario, Equipamento, Emprestimo
from app.forms import UsuarioForm, EquipamentoForm, EmprestimoForm
from app.enums import TIPO_USUARIO

def home(request: WSGIRequest) -> HttpResponse:
    return render(request, 'home.html', status=200)


def obter_usuarios(request: WSGIRequest) -> HttpResponse:
    usuarios: list[Usuario] = Usuario.objects.all()

    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios}, status=200)


def deletar_usuario(request: WSGIRequest, id: int) -> HttpResponse:
    usuario: Usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()

    return redirect(obter_usuarios) # 204 No Content


def atualizar_usuario(request: WSGIRequest, id: int) -> HttpResponse:
    usuario: Usuario = get_object_or_404(Usuario, id=id) 
    infos: list[str] = []
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()  
            return redirect(obter_usuarios) # 200 OK ou 204 No Content

        infos.append("Formulário Inválido!")

    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'usuarios/atualizar_usuario.html', {'form': form}, status=200)


def criar_usuario(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(obter_usuarios) # 201 Created
    else:
        form = UsuarioForm()

    return render(request, 'usuarios/criar_usuario.html', {'form': form}, status=200)


def obter_equipamentos(request: WSGIRequest) -> HttpResponse:
    equipamentos: list[Equipamento] = Equipamento.objects.all()

    return render(request, 'equipamentos/equipamentos.html', {'equipamentos': equipamentos}, status=200)


def deletar_equipamento(request: WSGIRequest, id: int) -> HttpResponse:
    equipamento: Equipamento = get_object_or_404(Equipamento, id=id)
    equipamento.delete()

    return redirect(obter_equipamentos) # 204 No Content


def atualizar_equipamento(request: WSGIRequest, id: int) -> HttpResponse:
    equipamento: Usuario = get_object_or_404(Equipamento, id=id) 
    infos: list[str] = []
    
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()  
            return redirect(obter_equipamentos) # 200 OK ou 204 No Content

        infos.append("Formulário Inválido!")

    else:
        form = EquipamentoForm(instance=equipamento)

    return render(request, 'equipamentos/atualizar_equipamento.html', {'form': form}, status=200)


def criar_equipamento(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(obter_equipamentos) # 201 Created
    else:
        form = EquipamentoForm()

    return render(request, 'equipamentos/criar_equipamento.html', {'form': form}, status=200)


def obter_emprestimos(request: WSGIRequest) -> HttpResponse:
    emprestimos: list[Emprestimo] = Emprestimo.objects.all()

    return render(request, 'emprestimos/emprestimos.html', {'emprestimos': emprestimos}, status=200)


def deletar_emprestimo(request: WSGIRequest, id: int) -> HttpResponse:
    emprestimo: Emprestimo = get_object_or_404(Emprestimo, id=id)
    emprestimo.delete()

    return redirect(obter_emprestimos) # 204 No Content


def atualizar_emprestimo(request: WSGIRequest, id: int) -> HttpResponse:
    emprestimo: Emprestimo = get_object_or_404(Emprestimo, id=id) 
    infos: list[str] = []
    
    if request.method == 'POST':

        # Verifica se o Usuário e o Equipamento existem
        id_usuario = request.POST.get('usuario')
        id_equipamento = request.POST.get('equipamento')
        quantidade_desejada = int(request.POST.get('quantidade', 1))

        usuario = Usuario.objects.filter(id=id_usuario).first()
        if not usuario:
            infos.append(f"Cliente com id={id_usuario} não existe!")

        equipamento = Equipamento.objects.filter(id=id_equipamento).first()
        if not equipamento:
            infos.append(f"Produto com id={id_equipamento} não existe!")

        # Regra de negócio
        continuar: bool = True
        if usuario and usuario.tipo != TIPO_USUARIO.get('Colaborador'):
            infos.append("Somente Colaboradores podem pedir Empréstimos!")
            continuar = False
        

        # Obtenha a quantidade total emprestada desse equipamento, exceto o empréstimo atual
        quantidade_emprestada = Emprestimo.objects.filter(equipamento_id=id_equipamento).exclude(id=emprestimo.id).aggregate(Sum('quantidade'))['quantidade__sum']
        
        # Caso não haja nenhum empréstimo do equipamento, o valor será None, então ajustamos para 0
        if quantidade_emprestada is None:
            quantidade_emprestada = 0

        # Quantidade disponível = quantidade total no estoque - quantidade já emprestada
        quantidade_disponivel = equipamento.quantidade - quantidade_emprestada

        # Valida se a quantidade desejada é possível
        if quantidade_desejada > quantidade_disponivel:
            continuar = False
            infos.append(f"O Equipamento {equipamento.nome} não possui estoque suficiente! Disponível: {quantidade_disponivel}")
        
        print(f"Quantidade emprestada: {quantidade_emprestada}")
        print(f"Quantidade disponível: {quantidade_disponivel}")
        print(f"Quantidade desejada: {quantidade_desejada}")
        print(f"Quantidade no estoque: {equipamento.quantidade}")
        
        # Se o Usuário e Equipamento existem, e as regras foram cumpridas, atualiza o Empréstimo
        if usuario and equipamento and continuar:
            emprestimo.usuario = usuario
            emprestimo.equipamento = equipamento
            emprestimo.quantidade = quantidade_desejada
            form = EmprestimoForm(request.POST, instance=emprestimo)

            if form.is_valid():
                form.save()
                return redirect(obter_emprestimos)  # Redireciona após sucesso
            else:
                # Adiciona os erros do formulário à lista de infos
                infos.append("Formulário Inválido!")
                for field in form:
                    for error in field.errors:
                        infos.append(f"{field.label}: {error}")
        else:
            form = EmprestimoForm(instance=emprestimo)
    else:
        form = EmprestimoForm(instance=emprestimo)

    context = {
        'form': form,
        'infos': infos,
    }

    return render(request, 'emprestimos/atualizar_emprestimo.html', context=context, status=200)


def criar_emprestimo(request: WSGIRequest) -> HttpResponse:
    infos: list[str] = []

    if request.method == 'POST':
        id_usuario: int = request.POST.get('usuario')

        continuar: bool = True
        usuario: Usuario = Usuario.objects.filter(id=id_usuario).first()
        if usuario.tipo != TIPO_USUARIO.get('Colaborador'):
            infos.append("Somente Colaboradores poder pedir Empréstimos!")
            continuar = False


        id_equipamento: int = request.POST.get('equipamento')
        equipamento = Equipamento.objects.get(id=id_equipamento)

        # Obtenha a quantidade total emprestada desse equipamento
        quantidade_emprestada = Emprestimo.objects.filter(equipamento_id=id_equipamento).aggregate(Sum('quantidade'))['quantidade__sum']
        # Caso não haja nenhum empréstimo do equipamento, o valor será None, então ajustamos para 0
        if quantidade_emprestada is None:
            quantidade_emprestada = 0

        # Quantidade disponível = quantidade total no estoque - quantidade emprestada
        quantidade_disponivel = equipamento.quantidade - (quantidade_emprestada + int(request.POST.get('quantidade')))

        if quantidade_disponivel < 0:
            continuar = False
            infos.append(f"O Equipamento {equipamento.nome} não possui estoque!")

        form = EmprestimoForm(request.POST)
        if form.is_valid() and continuar:
            form.save()
            return redirect(obter_emprestimos) # 201 Created
    else:
        form = EmprestimoForm()


    return render(request, 'emprestimos/criar_emprestimo.html', {'form': form, 'infos': infos}, status=200)
