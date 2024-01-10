from django.shortcuts import render, redirect
from .forms import LoginForm, RegistroForm
from django.http import Http404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def registro_view(request):
    registro_form_data = request.session.get('registro_form_data', None)
    form = RegistroForm(registro_form_data)
    return render(request, 'authors/pages/registro_view.html', {
        'form': form,
        'form_action': reverse('authors:registro_create'),
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
        return redirect(reverse('authors:login'))

    return redirect('authors:registro')


def login_view(request):
    form = LoginForm()
    return render(request, 'authors/pages/login.html', {
        'form': form,
        'form_action': reverse('authors:login_create'),
    })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    login_url = reverse('authors:login')

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Você está logado.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'nome de usuário ou senha inválidos')
    else:
        messages.error(request, 'Dados Invalidos')

    return redirect(login_url)


@login_required(login_url='authors:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('authors:login'))

    if request.POST.get('username') != request.user.username:
        return redirect(reverse('authors:login'))

    logout(request)
    return redirect(reverse('authors:login'))
