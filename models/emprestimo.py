from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Emprestimo(Base):
    __tablename__ = 'emprestimos'
    id = Column(Integer, primary_key=True)
    aluno_id = Column(Integer, ForeignKey('alunos.id'))
    livro_id = Column(Integer, ForeignKey('livros.id'))

    aluno = relationship("Aluno")
    livro = relationship("Livro")
