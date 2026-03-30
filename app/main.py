from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

# Modelo do filme
class Filme(BaseModel):
    id: int = None
    titulo: str
    diretor: str
    ano: int
    genero: str

# Banco de dados em memória (lista Python)
filmes_db = []
contador_id = 1

app = FastAPI(
    title="API de Filmes",
    description="CRUD de filmes - Versão Simplificada",
    version="1.0.0"
)

@app.get("/")
def raiz():
    return {
        "mensagem": "API de Filmes - Wattio",
        "endpoints": [
            "GET /filmes - Lista todos os filmes",
            "POST /filmes - Cadastra novo filme",
            "GET /filmes/{id} - Busca filme por ID"
        ]
    }

# Rota GET /filmes - Retorna todos os filmes
@app.get("/filmes", response_model=List[Filme])
def listar_filmes():
    return filmes_db

# Rota POST /filmes - Cadastra um novo filme
@app.post("/filmes", response_model=Filme, status_code=201)
def criar_filme(filme: Filme):
    global contador_id

    # Criar novo filme com ID automático
    novo_filme = filme.model_dump()
    novo_filme["id"] = contador_id
    contador_id += 1

    # Adicionar à lista
    filmes_db.append(novo_filme)

    return novo_filme

# Rota GET /filmes/{id} - Retorna filme específico
@app.get("/filmes/{id}", response_model=Filme)
def buscar_filme(id: int):
    for filme in filmes_db:
        if filme["id"] == id:
            return filme

    raise HTTPException(status_code=404, detail="Filme não encontrado")
