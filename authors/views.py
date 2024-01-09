from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.http import Http404
from django.contrib import messages


def registro_view(request):
    registro_form_data = request.session.get('registro_form_data', None)
    form = RegistroForm(registro_form_data)
    return render(request, 'authors/pages/registro_view.html', {
        'form': form,
    })


# este campo é para criar e salvar usuario no banco de dados.
def registro_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['registro_form_data'] = POST
    form = RegistroForm(POST)

    if form.is_valid():
        user = form.save(commit=False)  # aqui está salvando a senha em uma variavel, pois nao foi para a base de dados
        user.set_password(user.password)  # aqui está criptografando a senha
        user.save()  # aqui está salvando a senha na base de dados
        messages.success(request, 'Seu Usuario foi criado com sucesso, por favor faça Seu Login.')
        del(request.session['registro_form_data'])

    return redirect('authors:registro')
