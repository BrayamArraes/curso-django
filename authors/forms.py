from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re


def strong_password(password):
    # está linha é p/ o usuario criar a password com caracteres/numeros tendo que importar o re (expreçao regular): import re
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'a password deve ter pelo menos uma letra maiúscula, '
            'uma letra minúscula e um número. O comprimento deve ser '
            'pelo menos 8 caracteres.'
        ),
            code='invalid'
        )

# Dentro desta class vc pode colocar tudo de uma vez sem precisar usar os fields um por um entao dentro da variavel
# você pode colocar os placeholder, label, help-text, widget.... como exemplo abaixo .


class RegistroForm(forms.ModelForm):
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha'
        }),
        validators=[strong_password],
        label='Senha',
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repita sua senha'
        }),
        label='Confirme sua senha'
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
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
                'class': 'input text-input'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Digite seu Sobrenome',
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Digite seu E-mail',
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'Digite nome do Usuário',
            }),
        }

    # esta def clean garante que o e-mail seja unico
    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'Este e-mail já está em uso', code='invalid',
            )

        return email

    # este metodo é para validar um campo de formulario, o def clean é onde o formulario vai.
    def clean_password(self):
        data = self.cleaned_data.get('password')

        if 'atenção' in data:
            raise ValidationError(
                'Não digite %(value)s no campo senha',
                code='invalid',
                params={'value': '"atenção"'}
            )

        return data

    # este metodo é para validar apartir do clean_field que seria os name dos campos por exemplo first name
    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')

        if 'John Doe' in data:
            raise ValidationError(
                'Não digite %(value)s no campo first name',
                code='invalid',
                params={'value': '"John Doe"'}
            )

        return data

    # está validação é feita quando um campo depende de outro para validar por exemplo password e a confirmaçao da password 
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'password e password 2 devem ser iguais',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })
