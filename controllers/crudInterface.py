from abc import ABC, abstractmethod

class CrudInterface(ABC):

    @abstractmethod
    def adicionar(self, *args, **kwargs):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def remover(self, id):
        pass