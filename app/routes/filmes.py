from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/filmes", tags=["filmes"])

@router.get("/", response_model=List[schemas.FilmeResponse])
def listar_filmes(db: Session = Depends(get_db)):
    filmes = db.query(models.FilmeModel).all()
    return filmes

@router.post("/", response_model=schemas.FilmeResponse, status_code=201)
def criar_filme(filme: schemas.FilmeCreate, db: Session = Depends(get_db)):
    novo_filme = models.FilmeModel(**filme.model_dump())
    db.add(novo_filme)
    db.commit()
    db.refresh(novo_filme)
    return novo_filme

@router.get("/{id}", response_model=schemas.FilmeResponse)
def buscar_filme(id: int, db: Session = Depends(get_db)):
    filme = db.query(models.FilmeModel).filter(models.FilmeModel.id == id).first()
    
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    
    return filme
