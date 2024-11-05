from django import forms

from app.models import Historico
from app.utils.enums import StatusEmprestimo
from app.utils import obter_data_atual


class HistoricoForm(forms.ModelForm):

    class Meta:
        model = Historico
        fields = [
            'quantidade', 
            'status', 
            'observacao',
            'data_emprestimo', 
            'data_devolucao_efetiva', 
            'nome_equipamento', 
            'nome_usuario', 
        ]
        
        widgets = {
            'quantidade': forms.NumberInput(attrs={
                'placeholder': 'Quantidade',
                'min': '1',
            }),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Se o formulário é para criação (sem instância)
        if not self.instance.pk: 
            self.initial['data_devolucao_efetiva'] = obter_data_atual()

        self.fields['status'].choices = StatusEmprestimo.obter_status_para_arquivar()
        
        self.fields['quantidade'].required = False
        self.fields['nome_usuario'].required = False
        self.fields['data_emprestimo'].required = False
        self.fields['nome_equipamento'].required = False


    def save(self, commit=True):
        return super().save(commit=commit)
    