import uuid

from django.db import models
from django.utils.text import slugify

from app.models import Equipamento, Usuario
from app.utils import obter_data_atual, obter_data_do_proximo_mes
from app.utils.enums import StatusEmprestimo


class Emprestimo(models.Model):

    # Colunas da tabela 'Emprestimo'
    quantidade = models.PositiveIntegerField(default=1)
    status = models.CharField(
        max_length=20, 
        choices=StatusEmprestimo.obter_status_para_cadastro, 
        default=StatusEmprestimo.EMPRESTADO
    )
    data_emprestimo = models.DateTimeField(default=obter_data_atual)
    data_devolucao_prevista = models.DateTimeField(default=obter_data_do_proximo_mes)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, related_name='emprestimos')

    slug = models.SlugField(unique=True, blank=True)
    

    def __str__(self) -> str:
        return str(self.data_emprestimo)
    

    def save(self, *args, **kwargs) -> None:
        # Apenas gera o slug se não existir
        if not self.slug:  
            # Gera um slug com UUID
            self.slug = slugify(f"{uuid.uuid4()}")
            
        super().save(*args, **kwargs)
