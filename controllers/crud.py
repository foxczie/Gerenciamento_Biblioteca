from database.connection import session
from models.aluno import Aluno
from models.livro import Livro
from models.emprestimo import Emprestimo
from sqlalchemy.exc import IntegrityError
from utils.contador import Contador
from models.funcionario import Funcionario
from controllers.crudInterface import CrudInterface 

class Crud(CrudInterface):
    @staticmethod
    def adicionar_aluno(nome, email, matricula):
        try:
            novo = Aluno(nome=nome, email=email, matricula=matricula)
            session.add(novo)
            session.commit()
            print("Aluno adicionado com sucesso.")
            input('Aperte uma tecla para continuar...')
        except IntegrityError:
            session.rollback()
            print("Erro: Email ou matrícula já cadastrados.")
            input('Aperte uma tecla para continuar...')

    @staticmethod
    def listar_alunos():
        alunos = session.query(Aluno).all()
        for aluno in alunos:
            aluno.exibir_detalhes()
        input('Aperte uma tecla para continuar...')

    @staticmethod
    def remover_aluno(aluno_id):
        try:
            aluno = session.query(Aluno).filter_by(id=aluno_id).first()
            if aluno:
                session.delete(aluno)
                session.commit()
                print("Aluno removido com sucesso.")
                input('Aperte uma tecla para continuar...')
            else:
                print("Aluno não encontrado.")
                input('Aperte uma tecla para continuar...')
        except Exception as e:
            session.rollback()
            print(f"Erro ao remover aluno: {e}")
            input('Aperte uma tecla para continuar...')

    @staticmethod
    def adicionar_livro(titulo, autor):
        livro = Livro(titulo, autor)
        session.add(livro)
        session.commit()
        print("Livro adicionado com sucesso.")
        input('Aperte uma tecla para continuar...')

    @staticmethod
    def listar_livros():
        livros = session.query(Livro).all()
        livrosEmprestados = session.query(Emprestimo).all()
        
        idLivros = []

        for le in livrosEmprestados:
            idLivros.append(le.livro_id)
        
        for livro in livros:
            if livro.id not in idLivros:
                livro.exibir_info()
                
        print(Contador.mostrar_total())
        input('Aperte uma tecla para continuar...')

    @staticmethod
    def remover_livro(livro_id):
        try:
            livro = session.query(Livro).filter_by(id=livro_id).first()
            if livro:
                session.delete(livro)
                session.commit()
                print("Livro removido com sucesso.")
                input('Aperte uma tecla para continuar...')
            else:
                print("Livro não encontrado.")
                input('Aperte uma tecla para continuar...')
        except Exception as e:
            session.rollback()
            print(f"Erro ao remover livro: {e}")
            input('Aperte uma tecla para continuar...')

    @staticmethod
    def fazer_emprestimo(aluno_id, livro_id):
        try:
            aluno = session.query(Aluno).filter(Aluno.id == aluno_id).all()
            livro = session.query(Livro).filter(Livro.id == livro_id).all()
            
            if not aluno:
                print('Aluno não existe.')
                input('Aperte uma tecla para continuar...')
            elif not livro:
                print('Livro não disponível.')
                input('Aperte uma tecla para continuar...')
            else:
                emprestimo = Emprestimo(aluno_id=aluno_id, livro_id=livro_id)
                session.add(emprestimo)
                session.commit()
                print("Empréstimo realizado.")
                input('Aperte uma tecla para continuar...')

        except Exception as e:
            session.rollback()
            print(f"Erro ao realizar empréstimo: {e}")
            input('Aperte uma tecla para continuar...')

    @staticmethod
    def devolver_livro(emprestimo_id):
        try:
            emprestimo = session.query(Emprestimo).filter_by(id=emprestimo_id).first()
            if emprestimo:
                session.delete(emprestimo)
                session.commit()
                print("Livro devolvido com sucesso.")
                input('Aperte uma tecla para continuar...')
            else:
                print("Empréstimo não encontrado.")
                input('Aperte uma tecla para continuar...')
        except Exception as e:
            session.rollback()
            print(f"Erro ao devolver livro: {e}")
            input('Aperte uma tecla para continuar...')

    @staticmethod
    def listar_emprestimos():
        emprestimos = session.query(Emprestimo).all()
        if not emprestimos:
            print("Nenhum empréstimo registrado.")
            input('Aperte uma tecla para continuar...')
        for emp in emprestimos:
            print(f"[ID Empréstimo: {emp.id}] ID Aluno: {emp.aluno_id} | ID Livro: {emp.livro_id}")
        input('Aperte uma tecla para continuar...')
        
    @staticmethod
    def adicionar_funcionario(nome, email, cargo):
        try:
            novo = Funcionario(nome=nome, email=email, cargo=cargo)
            session.add(novo)
            session.commit()
            print("Funcionário adicionado com sucesso.")
            input('Aperte uma tecla para continuar...')
        except IntegrityError:
            session.rollback()
            print("Erro: Email já cadastrado.")
            input('Aperte uma tecla para continuar...')

    @staticmethod
    def listar_funcionarios():
        funcionarios = session.query(Funcionario).all()
        for func in funcionarios:
            func.exibir_detalhes()
        input('Aperte uma tecla para continuar...')

    @staticmethod
    def remover_funcionario(funcionario_id):
        try:
            funcionario = session.query(Funcionario).filter_by(id=funcionario_id).first()
            if funcionario:
                session.delete(funcionario)
                session.commit()
                print("Funcionário removido com sucesso.")
                input('Aperte uma tecla para continuar...')
            else:
                print("Funcionário não encontrado.")
                input('Aperte uma tecla para continuar...')
        except Exception as e:
            session.rollback()
            print(f"Erro ao remover funcionário: {e}")
            input('Aperte uma tecla para continuar...')