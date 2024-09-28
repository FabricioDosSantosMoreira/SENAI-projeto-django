from django import forms
from app.models import Usuario, Equipamento, Emprestimo
from app.enums import TIPO_USUARIO, CATEGORIA_EPI, CARGOS


class UsuarioForm(forms.ModelForm):

    class Meta:

        model = Usuario
        fields = ['nome', 'login', 'senha', 'tipo', 'cargo', 'data_admissao']
        widgets = {
            'tipo': forms.Select(
                choices=TIPO_USUARIO, 
                attrs={
                    'class': 'form-select',
                }
            ),
            'cargo': forms.Select(
                choices=CARGOS, 
                attrs={
                    'class': 'form-select',
                }
            ),
        }


class EquipamentoForm(forms.ModelForm):

    class Meta:
        
        model = Equipamento
        fields = ['nome', 'quantidade', 'validade', 'categoria']
        widgets = {
            'quantidade': forms.NumberInput(attrs={
                'placeholder': 'Quantidade',
                'min': '1',
            }),
            'categoria': forms.Select(
                choices=CATEGORIA_EPI, 
                attrs={
                    'class': 'form-select',
                }
            ),
        }


class EmprestimoForm(forms.ModelForm):

    class Meta:
    
        model = Emprestimo
        fields = ['data_emprestimo', 'data_devolucao', 'quantidade', 'usuario', 'equipamento']
        widgets = {
            'quantidade': forms.NumberInput(attrs={
                'placeholder': 'Quantidade',
                'min': '1',
            }),
        }
        