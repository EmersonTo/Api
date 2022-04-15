import string
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Api de uma Calculador Simples!!"}


class Resp(BaseModel):
    valor1: int
    valor2: int
    operacao: str


@app.post("/calculadora")
async def calculadora(resp: Resp):
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
