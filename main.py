"""API"""
from fastapi import FastAPI  # Importa a classe FastAPI() do pacote fastapi

app = FastAPI()  # Cria uma instância da classe FastAPI()


@app.get("/")  # Decorador para definir a rota raiz da API
def ola_mundo():
    """Olá mundo"""
    return {"mensagem": "Olá mundo!"}
