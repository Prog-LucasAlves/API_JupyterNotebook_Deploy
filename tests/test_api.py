"""Test API"""
from fastapi.testclient import TestClient

from app.main import app

# Teste de integração com o FastAPI.
client = TestClient(app)


def test_ola_mundo():
    response = client.get("/")
    assert response.status_code == 200


def test_ola_mundo_json():
    response = client.get("/")
    assert response.json() == {"mensagem": "Olá mundo!"}


def test_listar_produtos_status_code():
    response = client.get("/produtos")
    assert response.status_code == 200


def test_tamanho_da_lista_de_produtos():
    response = client.get("/produtos")
    assert len(response.json()) == 3


def test_pega_um_produto():
    response = client.get("/produtos/1")
    assert response.json() == {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um telefone que é inteligente",
        "preco": 1500.0,
    }