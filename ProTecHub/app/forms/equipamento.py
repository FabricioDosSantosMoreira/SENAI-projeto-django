from django import forms

from app.models import Equipamento
from app.utils.enums import CategoriaEPI


class EquipamentoForm(forms.ModelForm):

    class Meta:
        model = Equipamento
        fields = [
            'nome', 
            'categoria',
            'quantidade_total', 
            'validade',     
        ]

        widgets = {
            'quantidade_total': forms.NumberInput(attrs={
                'placeholder': 'Quantidade',
                'min': '1',
            }),
            'categoria': forms.Select(
                choices=CategoriaEPI, 
                attrs={
                    'class': 'form-select',
                }
            ),
        }
