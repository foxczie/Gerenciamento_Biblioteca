from sqlalchemy import Column, String, ForeignKey, Integer
from .pessoa import Pessoa

class Aluno(Pessoa):
    __tablename__ = 'alunos'
    id = Column(Integer, ForeignKey('pessoas.id'), primary_key=True)
    _matricula = Column("matricula", String, unique=True, nullable=False)

    __mapper_args__ = {'polymorphic_identity': 'aluno'}

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, valor):
        if len(valor) != 5:
            raise ValueError("A matrícula deve ter 5 caracteres.")
        self._matricula = valor

    def exibir_detalhes(self):
        print(f"Aluno: {self.nome}, Email: {self.email}, Matrícula: {self.matricula}, ID: {self.id}")
