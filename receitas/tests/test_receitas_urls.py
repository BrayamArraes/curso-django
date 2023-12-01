from django.test import TestCase
from django.urls import reverse


class ReceitaURLsTest(TestCase):
    def test_receita_home_url_esta_correta(self):
        url = reverse('receitas:home')
        self.assertEqual(url, '/')

    def test_receita_categoria_url_esta_correta(self):
        url = reverse('receitas:categoria', kwargs={'categoria_id': 1})
        self.assertEqual(url, '/receitas/categoria/1/')

    def test_receita_detalhe_url_esta_correta(self):
        url = reverse('receitas:receitas', kwargs={'id': 1})
        self.assertEqual(url, '/receitas/1/')