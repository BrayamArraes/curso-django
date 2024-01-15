from django import forms
from receitas.models import receita
from utils.django_forms import add_attr
from utils.strings import is_positive_number
from collections import defaultdict
from django.core.exceptions import ValidationError


class AuthorsReceitaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)

        add_attr(self.fields.get('preparation_steps'), 'class', 'span-2')

    class Meta:
        model = receita
        fields = 'title', 'description', 'preparation_time', \
            'preparation_time_unit', 'servings', 'servings_unit', \
            'preparation_steps', 'cover'
        widgets = {
            'cover': forms.FileInput(
                attrs={
                    'class': 'span-2'
                }
            ),
            'servings_unit': forms.Select(
                choices=(
                    ('Porções', 'Porções'),
                    ('Pedaços', 'Pedaços'),
                    ('Pessoas', 'Pessoas'),
                ),
            ),
            'preparation_time_unit': forms.Select(
                choices=(
                    ('Minutos', 'Minutos'),
                    ('Horas', 'Horas'),
                ),
            ),
        }
        labels = {
            'preparation_time_unit': 'Tempo de preparo (ex.: Minutos, Hora)',
            'cover': 'Imagem',
            'preparation_time': 'Tempo de preparo',
            'servings_unit': 'Tipos de porções',
            'servings': 'Quantidade de porções',
            'title': 'Titulo',
            'description': 'Descrição',
            'preparation_steps': 'Etapas de preparação',
        }

#  Tipo de validação
    def clean_preparation_time(self):
        field_name = 'preparation_time'
        field_value = self.cleaned_data.get(field_name)

        if not is_positive_number(field_value):
            self._my_errors[field_name].append('O número deve ser positivo.')

        return field_value

    def clean_servings(self):
        field_name = 'servings'
        field_value = self.cleaned_data.get(field_name)

        if not is_positive_number(field_value):
            self._my_errors[field_name].append('O número deve ser positivo.')

        return field_value
