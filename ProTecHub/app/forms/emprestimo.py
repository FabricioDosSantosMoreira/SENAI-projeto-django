from django import forms

from app.models import Emprestimo
from app.utils.enums import StatusEmprestimo


class EmprestimoForm(forms.ModelForm):

    class Meta:
        model = Emprestimo
        fields = [
            'quantidade', 
            'status', 
            'data_emprestimo', 
            'data_devolucao_prevista', 
            'usuario', 
            'equipamento',
        ]

        widgets = {
            'quantidade': forms.NumberInput(attrs={
                'placeholder': 'Quantidade',
                'min': '1',
            }),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['status'].choices = StatusEmprestimo.obter_status_para_cadastro()


    def save(self, commit=True):
        return super().save(commit=commit)
    