from django.db import models

from app.utils.enums import StatusEmprestimo
from app.utils import obter_data_atual


class Historico(models.Model):

    # Colunas da tabela 'Historico'
    quantidade = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20, 
        choices=StatusEmprestimo.obter_status_para_arquivar, 
        default=StatusEmprestimo.DEVOLVIDO
    )
    observacao = models.TextField()
    data_emprestimo = models.DateTimeField()
    data_devolucao_efetiva = models.DateTimeField(default=obter_data_atual, null=True)
    nome_equipamento = models.CharField(max_length=255) 
    nome_usuario = models.CharField(max_length=255) 


    def __str__(self) -> str:
        return str(self.data_emprestimo)
