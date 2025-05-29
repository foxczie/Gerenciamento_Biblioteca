from sqlalchemy import Column, Integer, String
from .base import Base

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    tipo = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'pessoa',
        'polymorphic_on': tipo
    }

    def exibir_detalhes(self):
        raise NotImplementedError("Subclasses devem implementar este método.")
