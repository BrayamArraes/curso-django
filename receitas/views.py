from django.shortcuts import render


def home(request):
    return render(request, 'receitas/pages/home.html', context={
        'nome': 'Brayam Arraes !',
    })


def receitas(request, id):
    return render(request, 'receitas/pages/receita-view.html', context={
        'nome': 'Brayam Arraes !',
    })
