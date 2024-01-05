"""Criação da API"""
from fastapi import FastAPI  # Importa a classe FastAPI() do pacote fastapi
from .routes import router  # Importa a classe Produto do arquivo routes.py

app = FastAPI()  # Cria uma instância da classe FastAPI()

app.include_router(router)  # Inclui o router na instância da classe FastAPI()
