"""API"""
from fastapi import FastAPI  # Importa a classe FastAPI() do pacote fastapi
from typing import List, Dict  # Importa as classes List e Dict do pacote typing

app = FastAPI()  # Cria uma instância da classe FastAPI()

# Lista de dicionários com os dados dos produtos.
produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um telefone que é inteligente",
        "preco": 1500.0,
     },
    {
        "id": 2,
        "nome": "Notebook",
        "descricao": "Um computador que é móvel",
        "preco": 3500.0,
     },
    {
        "id": 3,
        "nome": "Tablet",
        "descricao": "Um tablet que é móvel",
        "preco": 2500.0,
    }
]


# Decorador para definir a rota raiz da API
@app.get("/")
def ola_mundo():
    return {"mensagem": "Olá mundo!"}


# Rota para listar os produtos.
@app.get("/produtos")
def listar_produtos():
    return produtos
