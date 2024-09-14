from datetime import datetime, timedelta
from django.db import models
from app.enums import TIPO_USUARIO, CATEGORIA_EPI, CARGOS

def devolucao_padrao():
    return datetime.now() + timedelta(days=10)


class Usuario(models.Model):
    
    # Colunas
    nome = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    senha = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60, choices=TIPO_USUARIO)
    cargo = models.CharField(max_length=60, choices=CARGOS)
    data_admissao = models.DateTimeField(default=datetime.now)


    def __str__(self) -> str:
        return self.nome
    

class Equipamento(models.Model):

    # Colunas 
    nome = models.CharField(max_length=255) 
    quantidade = models.PositiveIntegerField(default=1)
    validade = models.DateTimeField(default=datetime.now)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_EPI)


    def __str__(self) -> str:
        return self.nome
    

class Emprestimo(models.Model):

    # Colunas
    data_emprestimo = models.DateTimeField(default=datetime.now)
    data_devolucao = models.DateTimeField(default=devolucao_padrao)
    quantidade = models.PositiveIntegerField(default=1)

    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.data_emprestimo
    