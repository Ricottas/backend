from pydantic import BaseModel

class FilmeCreate(BaseModel):
    titulo: str
    diretor: str
    ano: int
    genero: str

class FilmeResponse(FilmeCreate):
    id: int
    
    class Config:
        from_attributes = True
