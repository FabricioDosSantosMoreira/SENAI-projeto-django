from django import forms
from app.models import Usuario
from app.utils.enums import TipoUsuario, Cargos


class UsuarioForm(forms.ModelForm):

    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Usuario
        fields = [
            'nome', 
            'email', 
            'senha',
            'cargo',
            'tipo', 
            'foto', 
        ]
        
        widgets = {
            'tipo': forms.Select(
                choices=TipoUsuario, 
                attrs={
                    'class': 'form-select',
                }
            ),
            'cargo': forms.Select(
                choices=Cargos, 
                attrs={
                    'class': 'form-select',
                }
            ),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data['senha'])  # Define a senha de forma segura
        if commit:
            usuario.save()

        return usuario
