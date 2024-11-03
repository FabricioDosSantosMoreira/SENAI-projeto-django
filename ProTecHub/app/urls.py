from django.urls import path, URLPattern
from app import views

urlpatterns: list[URLPattern] = [

    # Views de 'base.py'
    path('', views.home, name='home'),
    path('cadastro/', views.cadastrar, name='cadastro'),
    path('logout/', views.deslogar, name='logout'),
    path('login/', views.logar, name='login'),

    # Views de 'outros.py'
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre, name='sobre'),

    # Views de 'interno.py'
    path('interno/home', views.interno, name='interno'),

    # Views de 'usuario.py'
    path('interno/usuarios/obter', views.obter_usuarios, name='obter_usuarios'),
    path('interno/usuarios/criar', views.criar_usuario, name='criar_usuario'),
    path('interno/usuarios/deletar/<int:id>', views.deletar_usuario, name='deletar_usuario'),
    path('interno/usuarios/atualizar/<int:id>', views.atualizar_usuario, name='atualizar_usuario'),

    # Views de 'equipamento.py'
    path('interno/equipamentos/obter', views.obter_equipamentos, name='obter_equipamentos'),
    path('interno/equipamentos/criar', views.criar_equipamento, name='criar_equipamento'),
    path('interno/equipamentos/deletar/<int:id>', views.deletar_equipamento, name='deletar_equipamento'),
    path('interno/equipamentos/atualizar/<int:id>', views.atualizar_equipamento, name='atualizar_equipamento'),

    # Views de 'emprestimos.py'
    path('interno/emprestimos/obter', views.obter_emprestimos, name='obter_emprestimos'),
    path('interno/emprestimos/criar', views.criar_emprestimo, name='criar_emprestimo'),
    path('interno/emprestimos/deletar/<int:id>', views.deletar_emprestimo, name='deletar_emprestimo'),
    path('interno/emprestimos/atualizar/<int:id>', views.atualizar_emprestimo, name='atualizar_emprestimo'),

    # Views de 'historico.py' 
    path('interno/historico/obter', views.obter_historico, name='obter_historico'),
    path('interno/historico/arquivar/<int:id_emprestimo>', views.arquivar_emprestimo_no_historico, name='arquivar_emprestimo_no_historico'),
    path('interno/historico/deletar/<int:id>', views.deletar_item_historico, name='deletar_item_historico'),
    path('interno/historico/atualizar/<int:id>', views.atualizar_item_historico, name='atualizar_item_historico'),
]
