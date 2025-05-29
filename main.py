from database.connection import engine
from models.base import Base
from controllers.crud import Crud

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
        [8] Adicionar Funcionário
        [9] Listar Funcionários
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
            Crud.adicionar_aluno(nome, email, matricula)

        elif opcao == 2:
            Crud.listar_alunos()

        elif opcao == 3:
            titulo = input("Título: ")
            autor = input("Autor: ")
            Crud.adicionar_livro(titulo, autor)

        elif opcao == 4:
            Crud.listar_livros()

        elif opcao == 5:
            try:
                aluno_id = int(input("ID do Aluno: "))
                livro_id = int(input("ID do Livro: "))
                Crud.fazer_emprestimo(aluno_id, livro_id)
            except ValueError:
                print("IDs devem ser numéricos.")

        elif opcao == 6:
            Crud.listar_emprestimos()

        elif opcao == 7:
            try:
                emprestimo_id = int(input("ID do Empréstimo: "))
                Crud.devolver_livro(emprestimo_id)
            except ValueError:
                print("ID inválido.")

        elif opcao == 8:
            nome = input("Nome: ")
            email = input("Email: ")
            cargo = input("Cargo: ")
            Crud.adicionar_funcionario(nome, email, cargo)

        elif opcao == 9:
            Crud.listar_funcionarios()

        elif opcao == 0:
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")

menu()