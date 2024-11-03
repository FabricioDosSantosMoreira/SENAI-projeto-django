from django.db import models
from django.db.models import Sum

from app.utils.enums import CategoriaEPI
from app.utils import obter_data_do_proximo_ano


class Equipamento(models.Model):

    # Colunas da tabela 'Equipamento'
    nome = models.CharField(max_length=255) 
    quantidade_total = models.PositiveIntegerField(default=1)
    validade = models.DateTimeField(default=obter_data_do_proximo_ano)
    categoria = models.CharField(max_length=100, choices=CategoriaEPI)


    @property
    def quantidade_disponivel(self) -> int:
        quantidade_emprestada = self.emprestimos.aggregate(Sum('quantidade')).get('quantidade__sum') or 0

        return self.quantidade_total - quantidade_emprestada


    def __str__(self) -> str:
        return self.nome
    