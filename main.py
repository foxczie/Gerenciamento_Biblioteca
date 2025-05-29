from database.connection import engine
from models.base import Base
from controllers import crud

# Criar tabelas
Base.metadata.create_all(engine)

def menu():
    while True:
        print("""
        [1] Adicionar Aluno
        [2] Listar Alunos
        [3] Adicionar Livro
        [4] Listar Livros
        [5] Realizar Empréstimo
        [6] Listar Empréstimos
        [7] Devolver Livro
        [0] Sair
        """)

        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if opcao == 1:
            nome = input("Nome: ")
            email = input("Email: ")
            matricula = input("Matrícula: ")
            crud.adicionar_aluno(nome, email, matricula)

        elif opcao == 2:
            crud.listar_alunos()

        elif opcao == 3:
            titulo = input("Título: ")
            autor = input("Autor: ")
            crud.adicionar_livro(titulo, autor)

        elif opcao == 4:
            crud.listar_livros()

        elif opcao == 5:
            try:
                aluno_id = int(input("ID do Aluno: "))
                livro_id = int(input("ID do Livro: "))
                crud.fazer_emprestimo(aluno_id, livro_id)
            except ValueError:
                print("IDs devem ser numéricos.")
        elif opcao == 6:
            crud.listar_emprestimos()

        elif opcao == 7:
            try:
                emprestimo_id = int(input("ID do Empréstimo: "))
                crud.devolver_livro(emprestimo_id)
            except ValueError:
                print("ID inválido.")

        elif opcao == 0:
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

# Iniciar menu
menu()
