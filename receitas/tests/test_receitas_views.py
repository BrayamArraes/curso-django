from django.test import TestCase
from django.urls import resolve, reverse
from receitas import views

class ReceitaViewsTest(TestCase):
    def test_receita_home_view_esta_correto(self):
        view = resolve(reverse('receitas:home'))
        self.assertIs(view.func, views.home)

    def test_receitas_categoria_view_function_esta_correta(self):
        view = resolve(
            reverse('receitas:categoria', kwargs={'categoria_id': 1})
        )
        self.assertIs(view.func, views.categoria)

    def test_receitas_detalhe_view_function_esta_correta(self):
        view = resolve(
            reverse('receitas:receitas', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.receitas)


    def test_receita_home_status(self):
        resposta = self.client.get(reverse('receitas:home'))
        self.assertEqual(resposta.status_code, 200)
