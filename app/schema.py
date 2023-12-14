"""Pydantic"""
from pydantic import BaseModel, PositiveInt  # Importa a classe BaseModel() do pacote pydantic
from typing import Optional  # Importa a classe Optional() do pacote typing.


# Classe para representar os dados dos produtos.
class ProdutosSchema(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: PositiveInt
