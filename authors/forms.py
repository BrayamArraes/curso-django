from django import forms
from django.contrib.auth.models import User


class RegistroForm(forms.ModelForm):
    senha = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repita sua Senha'
        })
        )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
    # label é o nome do campo que aparece para o usuario
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
    }
        # help_texts é a mensagem que fica embaixo do campo
        help_texts = {
            'username': 'Obrigatório. 30 caracteres ou menos. Letras, números e @/./+/-/_ apenas',
        }
        # é os erros dos campos e ele é por codigo exemplo: required, invalide
        error_messages = {
            'username': {
                'required': 'Este campo é obrigatório.',
            }
        }
        # widgets nada mais é de uma breve descrição do campo.. neste campo pode colocar placeholder, class de css .. para editar melhor
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Digite seu Nome',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Digite seu Sobrenome',
            }),
            'password': forms.PasswordInput(attrs={
                 'placeholder': 'Digite sua Senha',
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Digite seu E-mail',
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'Digite nome do Usuário',
            }),
        }