class Contador:
    __total_livros = 0  

    @classmethod
    def incrementar(cls):
        cls.__total_livros += 1

    @classmethod
    def mostrar_total(cls):
        return f"Total de livros: {cls.__total_livros}"
    
