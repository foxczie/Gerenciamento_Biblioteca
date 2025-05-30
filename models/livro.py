from sqlalchemy import Column, Integer, String
from .base import Base
from utils.contador import Contador

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        Contador.incrementar()

    def exibir_info(self):
        print(f"Livro: {self.titulo} | Autor: {self.autor} | ID: {self.id}")
