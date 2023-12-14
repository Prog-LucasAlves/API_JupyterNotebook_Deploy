"""API"""
from fastapi import FastAPI  # Importa a classe FastAPI() do pacote fastapi
from .schema import ProdutosSchema  # Importa a classe Produto do arquivo schema.py
from .data import Produtos  # Importa a lista de produtos do arquivo data.py

app = FastAPI()  # Cria uma instância da classe FastAPI()

lista_de_produtos = Produtos()


# Decorador para definir a rota raiz da API
@app.get("/")
def ola_mundo():
    return {"mensagem": "Olá mundo!"}


# Rota para listar os produtos.
@app.get("/produtos", response_model=list[ProdutosSchema])
def listar_produtos():
    return lista_de_produtos.listar_produtos()


# Rota para obter um produto específico.
@app.get("/produtos/{id}", response_model=ProdutosSchema)
def obter_produto(id: int):
    return lista_de_produtos.buscar_produto(id)


@app.post("/produtos", response_model=ProdutosSchema)
def adicionar_produto(produto: ProdutosSchema):
    return lista_de_produtos.adicionar_produto(produto.model_dump())
