class Contador:
    total_livros = 0

    @classmethod
    def mostrar_total(cls):
        return f"Total de livros: {cls.total_livros}"
