from django.shortcuts import render


def home(request):
    return render(request, 'receitas/home.html', context={
        'nome': 'Brayam Arraes !',
    })
