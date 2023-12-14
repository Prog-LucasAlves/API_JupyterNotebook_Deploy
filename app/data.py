"""Data"""
from typing import List, Dict  # Importa as classes List e Dict do pacote typing


class Produtos:
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
        },
    ]

    def listar_produtos(self):
        return self.produtos

    def buscar_produto(self, id):
        for produto in self.produtos:
            if produto["id"] == id:
                return produto
        return {"Status": 404, "mensagem": "Produto não encontrado."}

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        return produto
