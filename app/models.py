from sqlalchemy import Column, Integer, String
from .database import Base

class FilmeModel(Base):
    __tablename__ = "filmes"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False, index=True)
    diretor = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    genero = Column(String, nullable=False)
    
    def __repr__(self):
        return f"<Filme(id={self.id}, titulo='{self.titulo}')>"
