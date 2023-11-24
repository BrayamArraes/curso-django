from django.shortcuts import render, get_list_or_404
from utils.receitas.factory import make_receitas
from receitas.models import receita



def home(request):
    receitas = receita.objects.filter(is_published=True).order_by('-id')
    return render(request, 'receitas/pages/home.html', context={
        'receitas': receitas,
    })



def categoria(request, categoria_id):
    receitas = receita.objects.filter(category__id=categoria_id, is_published=True).order_by('-id')
    return render(request, 'receitas/pages/categoria.html', context={
        'receitas': receitas,
    })



def receitas(request, id):
    receitas = receita.objects.filter(
        pk=id,
        is_published=True,
    ).order_by('-id').first()

    return render(request, 'receitas/pages/receita-view.html', context={
        'receita': receitas,
        'is_detalhe_page': True
    })


