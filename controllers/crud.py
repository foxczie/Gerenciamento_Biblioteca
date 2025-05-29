from database.connection import session
from models.aluno import Aluno
from models.livro import Livro
from models.emprestimo import Emprestimo
from sqlalchemy.exc import IntegrityError
from utils.contador import Contador

def adicionar_aluno(nome, email, matricula):
    try:
        novo = Aluno(nome=nome, email=email, matricula=matricula)
        session.add(novo)
        session.commit()
        print("Aluno adicionado com sucesso.")
    except IntegrityError:
        session.rollback()
        print("Erro: Email ou matrícula já cadastrados.")

def listar_alunos():
    alunos = session.query(Aluno).all()
    for aluno in alunos:
        aluno.exibir_detalhes()

def adicionar_livro(titulo, autor):
    livro = Livro(titulo, autor)
    session.add(livro)
    session.commit()
    print("Livro adicionado com sucesso.")

def listar_livros():
    livros = session.query(Livro).all()
    for livro in livros:
        livro.exibir_info()
    print(Contador.mostrar_total())

def fazer_emprestimo(aluno_id, livro_id):
    try:
        emprestimo = Emprestimo(aluno_id=aluno_id, livro_id=livro_id)
        session.add(emprestimo)
        session.commit()
        print("Empréstimo realizado.")
    except Exception as e:
        session.rollback()
        print(f"Erro ao realizar empréstimo: {e}")

def devolver_livro(emprestimo_id):
    try:
        emprestimo = session.query(Emprestimo).filter_by(id=emprestimo_id).first()
        if emprestimo:
            session.delete(emprestimo)
            session.commit()
            print("Livro devolvido com sucesso.")
        else:
            print("Empréstimo não encontrado.")
    except Exception as e:
        session.rollback()
        print(f"Erro ao devolver livro: {e}")

def listar_emprestimos():
    emprestimos = session.query(Emprestimo).all()
    if not emprestimos:
        print("Nenhum empréstimo registrado.")
    for emp in emprestimos:
        print(f"[ID: {emp.id}] Aluno: {emp.aluno.nome} | Livro: {emp.livro.titulo}")
    