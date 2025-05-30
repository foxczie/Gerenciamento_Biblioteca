from sqlalchemy import Column, String, ForeignKey, Integer
from .pessoa import Pessoa

class Funcionario(Pessoa):
    __tablename__ = 'funcionarios'
    id = Column(Integer, ForeignKey('pessoas.id'), primary_key=True)
    cargo = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'funcionario'
    }

    def exibir_detalhes(self):
        print(f"Funcionário: {self.nome}, Cargo: {self.cargo}, ID: {self.id}")
