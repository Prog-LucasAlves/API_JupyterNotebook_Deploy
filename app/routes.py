"""Routes API"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .schema import ProdutosSchema
from .config import get_db
from .model import Produto

router = APIRouter()


@router.get("/")
def produtos():
    return {"message": "Produtos API"}


# Rota para listar os produtos.
@router.get("/produtos", response_model=list[ProdutosSchema])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all()


# Rota para obter um produto específico.
@router.get("/produtos/{id}", response_model=ProdutosSchema)
def obter_produto(id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if produto:
        return produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")


# Rota para adicionar um produto.
@router.post("/produtos", response_model=ProdutosSchema, status_code=201)
def adicionar_produto(produto: ProdutosSchema, db: Session = Depends(get_db)):
    db_produto = Produto(**produto.model_dump())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto


# Rota para deletar um produto.
@router.delete("/produtos/{id}", response_model=ProdutosSchema)
def deletar_produto(id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if produto:
        db.delete(produto)
        db.commit()
        return produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")


# Rota para atualizar um produto.
@router.put("/produtos/{id}", response_model=ProdutosSchema)
def atualizar_produto(id: int, produto: ProdutosSchema, db: Session = Depends(get_db)):
    db_produto = db.query(Produto).filter(Produto.id == id).first()
    if db_produto:
        for key, value in produto.model_dump().items():
            setattr(db_produto, key, value) if value else None
        db.commit()
        db.refresh(db_produto)
        return db_produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
