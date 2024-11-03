from django.db import models

from app.models import Equipamento, Usuario
from app.utils.enums import StatusEmprestimo
from app.utils import obter_data_atual, obter_data_do_proximo_mes


class Emprestimo(models.Model):

    # Colunas da tabela 'Emprestimo'
    data_emprestimo = models.DateTimeField(default=obter_data_atual)
    data_devolucao_prevista = models.DateTimeField(default=obter_data_do_proximo_mes)
    quantidade = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=StatusEmprestimo.obter_status_para_cadastro, default=StatusEmprestimo.EMPRESTADO)

    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, related_name='emprestimos')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return str(self.data_emprestimo)
