from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),

    # Usuários
    path('usuarios/obter', views.obter_usuarios, name='obter_usuarios'),
    path('usuarios/criar', views.criar_usuario, name='criar_usuario'),
    path('usuarios/atualizar/<int:id>', views.atualizar_usuario, name='atualizar_usuario'),
    path('usuarios/deletar/<int:id>', views.deletar_usuario, name='deletar_usuario'),

    # Equipamentos
    path('equipamentos/obter', views.obter_equipamentos, name='obter_equipamentos'),
    path('equipamentos/criar', views.criar_equipamento, name='criar_equipamento'),
    path('equipamentos/atualizar/<int:id>', views.atualizar_equipamento, name='atualizar_equipamento'),
    path('equipamentos/deletar/<int:id>', views.deletar_equipamento, name='deletar_equipamento'),

    # Empréstimos
    path('emprestimos/obter', views.obter_emprestimos, name='obter_emprestimos'),
    path('emprestimos/criar', views.criar_emprestimo, name='criar_emprestimo'),
    path('emprestimos/atualizar/<int:id>', views.atualizar_emprestimo, name='atualizar_emprestimo'),
    path('emprestimos/deletar/<int:id>', views.deletar_emprestimo, name='deletar_emprestimo'),
]