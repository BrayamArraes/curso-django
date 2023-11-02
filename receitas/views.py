from django.shortcuts import render
from utils.receitas.factory import make_receitas

def home(request):
    return render(request, 'receitas/pages/home.html', context={
        'receitas': [make_receitas () for _ in range(10)],
    })


def receitas(request, id):
    return render(request, 'receitas/pages/receita-view.html', context={
        'receita': make_receitas(),
        'is_detalhe_page': True
    })
