"""Database Modeling"""
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

# Criando a base de dados
Base = declarative_base()


# Criando a tabela de produtos
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
