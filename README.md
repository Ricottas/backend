# API de Filmes - Desafio Wattio

API REST para gerenciamento de filmes, desenvolvida com FastAPI, SQLAlchemy e Docker.

## Tecnologias Utilizadas
- Python 3.14
- FastAPI
- SQLAlchemy (ORM)
- SQLite (persistência em arquivo)
- Docker / Docker Compose

## Como Executar

### Pré-requisitos
- Docker e Docker Compose instalados
- Docker Desktop aberto

### Passos

1. Clone o repositório:
```bash
git clone <seu-repositorio>
cd BACKEND

2. Execute o Docker Compose:
docker-compose up --build

3. Acesse a documentação da API:
http://localhost:8000/docs

Endpoints
Método	Endpoint	Descrição
GET	/	Informações da API
GET	/filmes	Lista todos os filmes
POST	/filmes	Cadastra novo filme
GET	/filmes/{id}	Busca filme por ID

Exemplo de Cadastro (POST/filmes)
Request Body:
{
  "titulo": "Matrix",
  "diretor": "Lana Wachowski",
  "ano": 1999,
  "genero": "Ficção Científica"
}

Response:
{
  "id": 1,
  "titulo": "Matrix",
  "diretor": "Lana Wachowski",
  "ano": 1999,
  "genero": "Ficção Científica"
}
