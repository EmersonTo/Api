"""
api de uma calculadora simples
"""
from typing import Optional  # pylint: disable=unused-import
from fastapi import FastAPI  # pylint: disable=E0401
from fastapi.responses import JSONResponse  # pylint: disable=E0401  W0611
from pydantic import BaseModel  # pylint: disable=E0401

app = FastAPI()


@app.get("/")
async def root():
    """
    mensagem de teste da rota principal da api
    """
    return {"message": "Api de uma Calculador Simples!!"}


class Resp(BaseModel):  # pylint: disable=R0903
    """
    Criando as variaveis para API
    """
    valor1: int
    valor2: int
    operacao: str


@app.post("/calculadora")
async def calculadora(resp: Resp):
    """
    rota calculadora onde será retornado o resultado do calculo
    """
    if resp.operacao == "+":
        resultado = resp.valor1 + resp.valor2
    elif resp.operacao == "-":
        resultado = resp.valor1 - resp.valor2
    elif resp.operacao == "*":
        resultado = resp.valor1 * resp.valor2
    elif resp.operacao == "/":
        resultado = resp.valor1 / resp.valor2
    else:
        resultado = "OPERADOR INVÁLIDO, ENVIE UM DOS SEGUINTE OPERADORES + - * /"

    return resultado
