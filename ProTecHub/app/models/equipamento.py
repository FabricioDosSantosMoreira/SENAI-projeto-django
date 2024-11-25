import uuid

from django.db import models
from django.db.models import Sum
from django.utils.text import slugify

from app.utils import obter_data_do_proximo_ano
from app.utils.enums import CategoriaEPI


class Equipamento(models.Model):

    # Colunas da tabela 'Equipamento'
    nome = models.CharField(max_length=255) 
    categoria = models.CharField(max_length=100, choices=CategoriaEPI.choices)
    quantidade_total = models.PositiveIntegerField(default=1)
    validade = models.DateField(default=obter_data_do_proximo_ano)
    
    slug = models.SlugField(unique=True, blank=True)
    
    
    @property
    def quantidade_disponivel(self) -> int:
        quantidade_emprestada = self.emprestimos.aggregate(Sum('quantidade')).get('quantidade__sum') or 0

        return self.quantidade_total - quantidade_emprestada


    def __str__(self) -> str:
        return self.nome
    

    def save(self, *args, **kwargs) -> None:
        # Apenas gera o slug se não existir
        if not self.slug:  
            # Gera um slug com UUID
            self.slug = slugify(f"{uuid.uuid4()}")
            
        super().save(*args, **kwargs)

    