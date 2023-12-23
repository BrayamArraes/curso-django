from django.shortcuts import render
from receitas.models import receita
from django.http.response import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from utils.pagination import make_pagination_range


def home(request):
    receitas = receita.objects.filter(is_published=True).order_by('-id')

    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

    paginator = Paginator(receitas, 9)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        paginator.page_range,
        4,
        current_page
        )

    return render(request, 'receitas/pages/home.html', context={
         'receitas': page_obj,
         'pagination_range': pagination_range,
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


def search(request):
    search_term = request.GET.get('search', '').strip()

    if not search_term:
        raise Http404()
    
    # Q significa trocar o AND 'E' para o OR 'OU' tendo que importar from django.db.models import Q 
    # order.by('-id') significa ordernar os ids na ordem decrescente
    receitas = receita.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')
     
    return render(request, 'receitas/pages/search.html', {
        'page_title': f'Pesquisa por "{search_term}"',
        'search_term': search_term,
        'receitas': receitas,
        })
      

