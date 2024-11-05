from django.db import models
from django.db.models import Sum

from app.utils.enums import CategoriaEPI
from app.utils import obter_data_do_proximo_ano


class Equipamento(models.Model):

    # Colunas da tabela 'Equipamento'
    nome = models.CharField(max_length=255) 
    categoria = models.CharField(max_length=100, choices=CategoriaEPI)
    quantidade_total = models.PositiveIntegerField(default=1)
    validade = models.DateField(default=obter_data_do_proximo_ano)
    
    
    @property
    def quantidade_disponivel(self) -> int:
        quantidade_emprestada = self.emprestimos.aggregate(Sum('quantidade')).get('quantidade__sum') or 0

        return self.quantidade_total - quantidade_emprestada


    def __str__(self) -> str:
        return self.nome
    