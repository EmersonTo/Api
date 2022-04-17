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
        resp_soma = post(self.url + "/calculadora",
                    json={"valor1": 11, "valor2": 6, "operacao": "+", "tipo": "POST"})
        message_soma = loads(resp_soma.text)
        resposta_esperada_soma = 17

        resp_subtracao = post(self.url + "/calculadora",
                    json={"valor1": 11, "valor2": 6, "operacao": "-", "tipo": "POST"})
        message_subtracao = loads(resp_subtracao.text)
        resposta_esperada_subtracao = 5

        resp_mutiplicacao = post(self.url + "/calculadora",
                    json={"valor1": 11, "valor2": 6, "operacao": "*", "tipo": "POST"})
        message_mutiplicacao = loads(resp_mutiplicacao.text)
        resposta_esperada_mutiplicacao = 66

        resp_divisao = post(self.url + "/calculadora",
                    json={"valor1": 60, "valor2": 6, "operacao": "/", "tipo": "POST"})
        message_divisao = loads(resp_divisao.text)
        resposta_esperada_divisao = 10

        resp_invalido = post(self.url + "/calculadora",
                    json={"valor1": 60, "valor2": 6, "operacao": "a", "tipo": "POST"})
        message_invalido = loads(resp_invalido.text)
        resposta_esperada_invalido = "OPERADOR INVÁLIDO, ENVIE UM DOS SEGUINTE OPERADORES + - * /"


        assert message_soma == resposta_esperada_soma
        assert message_subtracao == resposta_esperada_subtracao
        assert message_mutiplicacao == resposta_esperada_mutiplicacao
        assert message_divisao  == resposta_esperada_divisao
        assert message_invalido  == resposta_esperada_invalido
