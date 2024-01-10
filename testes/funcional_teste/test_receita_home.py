from django.test import LiveServerTestCase
from utils.browser import make_chrome_browser
import time
from selenium.webdriver.common.by import By


class ReceitaBaseFuncional(LiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=3):
        time.sleep(seconds)


class ReceitaHomeFuncional(ReceitaBaseFuncional):
    def test_receita_mensagem_nao_a_cadastro_de_receita(self):
        browser = self.browser
        browser.get(self.live_server_url)
        body = browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Não há cadastro de receitas aqui !', body.text)


class AuthorsRegistro(ReceitaBaseFuncional):
    def test_the_test(self):
        self.browser.get(self.live_server_url + '/authors/registro/')
        form = self.browser.find_element(
            By.XPATH,
            '/html/body/div[3]/form'
        )
