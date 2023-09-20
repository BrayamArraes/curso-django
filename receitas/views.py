from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'receitas/home.html', context={
        'nome': 'Brayam Arraes !',
    })


def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')
