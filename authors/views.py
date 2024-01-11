from django.shortcuts import render, redirect
from .forms import LoginForm, RegistroForm, AuthorsReceitaForm
from django.http import Http404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from receitas.models import receita


# pagina de registro/formulario
def registro_view(request):
    registro_form_data = request.session.get('registro_form_data', None)
    form = RegistroForm(registro_form_data)
    return render(request, 'authors/pages/registro_view.html', {
        'form': form,
        'form_action': reverse('authors:registro_create'),
    })


# def para pagina de criaçao de cadastro/salvando os dados na base.
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


# pagina de login e senha
def login_view(request):
    form = LoginForm()
    return render(request, 'authors/pages/login.html', {
        'form': form,
        'form_action': reverse('authors:login_create'),
    })


# pagina para logar seu usuario valido com senha
def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

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

    return redirect(reverse('authors:dashboard'))


@login_required(login_url='authors:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('authors:login'))

    if request.POST.get('username') != request.user.username:
        return redirect(reverse('authors:login'))

    logout(request)
    return redirect(reverse('authors:login'))


# entrando na dashboard ja logodo com seu usuario
@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard(request):
    receitas = receita.objects.filter(
        is_published=False,
        author=request.user,
    )
    return render(request, 'authors/pages/dashboard.html', {
        'receitas': receitas,
    })


# editando receitas
@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_receita_edit(request, id):
    receitas = receita.objects.filter(
        is_published=False,
        author=request.user,
        pk=id,
    ).first()

    if not receitas:
        raise Http404

    form = AuthorsReceitaForm(
        # dados de texto/objetos vai em request.POST
        data=request.POST or None,
        # files recebe arquivos binarios ou seja arquivos que nao estao em formato de texto.
        files=request.FILES or None,
        instance=receitas)

    if form.is_valid():
        # Agora, o form é valido e eu posso tentar salvar
        receitas = form.save(commit=False)

        receitas.author = request.user
        receitas.preparation_steps_is_html = False
        receitas.is_published = False

        receitas.save()

        messages.success(request, 'Sua receita foi salva com sucesso!')
        return redirect(reverse('authors:dashboard_receita_edit', args=(id,)))


    return render(request, 'authors/pages/dashboard_receita.html', {
        'form': form,
})


# NOVA RECEITA
@login_required(login_url='authors:login', redirect_field_name='next')
def criar_receita(request):
    form = AuthorsReceitaForm(
        data=request.POST or None,
        files=request.FILES or None,
    )

    if form.is_valid():
        receitas: receita = form.save(commit=False)

        receitas.author = request.user
        receitas.preparation_steps_is_html = False
        receitas.is_published = False

        receitas.save()

        messages.success(request, 'Salvo com sucesso!')
        return redirect(
            reverse('authors:dashboard_receita_edit', args=(receita.id,))
        )

    return render(
        request,
        'authors/pages/dashboard_receita.html',
        context={
            'form': form,
            'form_action': reverse('authors:criar_receita')
        }
    )


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_receita_delete(request):
    if not request.POST:
        raise Http404

    POST = request.POST
    id = POST.get('id')

    receitas = receita.objects.filter(
        is_published=False,
        author=request.user,
        pk=id,
    ).first()

    if not receitas:
        raise Http404()

    receitas.delete()
    messages.success(request, 'Receita Deletada com sucesso!')
    return redirect(reverse('authors:dashboard'))
