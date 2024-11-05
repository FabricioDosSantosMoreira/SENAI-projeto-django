from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

from app.utils.enums import TipoUsuario, Cargos


class Usuario(AbstractUser):

    # Colunas da tabela 'Usuario'
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cargo = models.CharField(max_length=24, choices=Cargos)
    tipo = models.CharField(max_length=24, choices=TipoUsuario)
    foto = models.ImageField(upload_to='usuarios/', null=True, blank=True)
    data_admissao = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs) -> None:
        # NOTE: O Django obriga a ter um 'username' quando herda de 'AbstractUser'
        if not self.username:  
            self.username = self.email  

        super().save(*args, **kwargs)

        # Atribuindo 'Roles' aos Usuários
        if self.tipo == TipoUsuario.ADMINISTRADOR:
            admin_group = Group.objects.get(name='Admin')
            self.groups.add(admin_group)
            
        elif self.tipo == TipoUsuario.SUPERVISOR:
            supervisor_group = Group.objects.get(name='Supervisor')
            self.groups.add(supervisor_group)

        elif self.tipo == TipoUsuario.COLABORADOR:
            colaborador_group = Group.objects.get(name='Colaborador')
            self.groups.add(colaborador_group)

        super().save(*args, **kwargs)


    def validar_senha(self, senha) -> bool:
        return check_password(senha, self.password)


    def __str__(self) -> str:
        return self.nome
    