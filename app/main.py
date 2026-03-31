from fastapi import FastAPI
from .routes import filmes
from .database import engine, Base

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Filmes",
    description="CRUD de filmes com FastAPI, SQLite e persistência",
    version="2.0.0"
)

# Incluir rotas
app.include_router(filmes.router)

@app.get("/")
def raiz():
    return {
        "mensagem": "API de Filmes - Wattio",
        "versao": "2.0.0",
        "persistencia": "SQLite com arquivo",
        "endpoints": [
            "GET /filmes - Lista todos os filmes",
            "POST /filmes - Cadastra novo filme",
            "GET /filmes/{id} - Busca filme por ID"
        ]
    }
