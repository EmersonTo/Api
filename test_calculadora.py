"""
testar a API CALCULADORA
"""
from json import loads  # pylint: disable=invalid-name
from requests import get, post


class TestCalculadora:
    """
    Classe de teste da calculadora
    """

    def setup(self):
        """
        recebe a url do api
        """
        self.url = "http://127.0.0.1:8000"  # pylint: disable=W0201

    def test_APIstatus(self):  # pylint: disable=invalid-name
        """
        testar se api estar funcionando
        """
        resp = get(self.url)
        assert resp.ok

    def test_APIresponse(self):  # pylint: disable=invalid-name
        """
        testar a mensagem de responsta da api
        """
        resp = get(self.url)
        message = loads(resp.text)
        assert message["message"] == "Api de uma Calculador Simples!!"

    def test_POSTmethod(self):  # pylint: disable=invalid-name
        """
        testar post SOMA
        """
        respSoma = post(self.url + "/calculadora",
                    json={"valor1": 11, "valor2": 6, "operacao": "+", "tipo": "POST"})
        message = loads(respSoma.text)
        resposta_esperada = 17
        assert message == resposta_esperada
