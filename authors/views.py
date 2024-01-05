from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.http import Http404


def registro_view(request):
    registro_form_data = request.session.get('registro_form_data', None)
    form = RegistroForm(registro_form_data)
    return render(request, 'authors/pages/registro_view.html', {
        'form': form,
    })


def registro_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['registro_form_data'] = POST
    form = RegistroForm(POST)

    return redirect('authors:registro')
