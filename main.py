from database.connection import engine
from models.base import Base
from controllers.crud import Crud
import os

Base.metadata.create_all(engine)

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("""
        === GERENCIAMENTO DE BIBLIOTECA ===

        [1] Adicionar Aluno
        [2] Listar Alunos
        [3] Remover Aluno

        [4] Adicionar Livro
        [5] Listar Livros
        [6] Remover Livro

        [7] Realizar Empréstimo
        [8] Listar Empréstimos
        [9] Devolver Livro

        [10] Adicionar Funcionário
        [11] Listar Funcionários
        [12] Remover Funcionário

        [0] Sair
        """)

        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            input('Aperte uma tecla para continuar...')
            continue

        if opcao == 1:
            nome = input("Nome: ")
            email = input("Email: ")
            matricula = input("Matrícula: ")
            Crud.adicionar_aluno(nome, email, matricula)
            input('Aperte uma tecla para continuar...')

        elif opcao == 2:
            Crud.listar_alunos()
            input('Aperte uma tecla para continuar...')

        elif opcao == 3:
            try:
                aluno_id = int(input("ID do Aluno a remover: "))
                Crud.remover_aluno(aluno_id)
            except ValueError:
                print("ID inválido.")
            input('Aperte uma tecla para continuar...')

        elif opcao == 4:
            titulo = input("Título: ")
            autor = input("Autor: ")
            Crud.adicionar_livro(titulo, autor)
            input('Aperte uma tecla para continuar...')

        elif opcao == 5:
            Crud.listar_livros()
            input('Aperte uma tecla para continuar...')

        elif opcao == 6:
            try:
                livro_id = int(input("ID do Livro a remover: "))
                Crud.remover_livro(livro_id)
            except ValueError:
                print("ID inválido.")
            input('Aperte uma tecla para continuar...')

        elif opcao == 7:
            try:
                aluno_id = int(input("ID do Aluno: "))
                livro_id = int(input("ID do Livro: "))
                Crud.fazer_emprestimo(aluno_id, livro_id)
            except ValueError:
                print("IDs devem ser numéricos.")
            input('Aperte uma tecla para continuar...')

        elif opcao == 8:
            Crud.listar_emprestimos()
            input('Aperte uma tecla para continuar...')

        elif opcao == 9:
            try:
                emprestimo_id = int(input("ID do Empréstimo: "))
                Crud.devolver_livro(emprestimo_id)
            except ValueError:
                print("ID inválido.")
            input('Aperte uma tecla para continuar...')

        elif opcao == 10:
            nome = input("Nome: ")
            email = input("Email: ")
            cargo = input("Cargo: ")
            Crud.adicionar_funcionario(nome, email, cargo)
            input('Aperte uma tecla para continuar...')

        elif opcao == 11:
            Crud.listar_funcionarios()
            input('Aperte uma tecla para continuar...')

        elif opcao == 12:
            try:
                funcionario_id = int(input("ID do Funcionário a remover: "))
                Crud.remover_funcionario(funcionario_id)
            except ValueError:
                print("ID inválido.")
            input('Aperte uma tecla para continuar...')

        elif opcao == 0:
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")
            input('Aperte uma tecla para continuar...')

menu()
