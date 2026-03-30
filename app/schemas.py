from pydantic import BaseModel

class FilmeCreate(BaseModel):
    titulo: str
    diretor: str
    ano: int
    genero: str

class FilmeResponse(BaseModel):
    id: int
    titulo: str
    diretor: str
    ano: int
    genero: str
    
    class Config:
        from_attributes = True
