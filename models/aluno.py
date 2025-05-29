from sqlalchemy import Column, String, ForeignKey, Integer
from .pessoa import Pessoa

class Aluno(Pessoa):
    __tablename__ = 'alunos'
    id = Column(Integer, ForeignKey('pessoas.id'), primary_key=True)
    matricula = Column(String, unique=True, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'aluno'
    }

    def exibir_detalhes(self):
        print(f"Aluno: {self.nome}, Email: {self.email}, Matrícula: {self.matricula}")
