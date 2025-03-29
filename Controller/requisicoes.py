from Controller.conexao import db_connect
from Models.professor import Professor
from Models.aluno import Aluno
from sqlalchemy import text
import os

def select_all(param: str) -> None:
    query = text(f"SELECT * FROM {param}")
    session = db_connect()
    try:
        registros = session.execute(query).fetchall()
        if len(registros)<1:
            print('Nenhum registro encontrado')
            input('')
        else:
            for row in registros:
                print(row)
            input('')
    finally:
        session.close()

def select_cpf(param: str, cpf: str) -> None:
    query = text(f"SELECT * FROM {param} WHERE cpf = :cpf")
    session = db_connect()
    try:
        registros = session.execute(query, {"cpf": cpf}).fetchall()
        if len(registros)<1:
            print('Nenhum registro encontrado')
            input('')
        else:
            for row in registros:
                print(row)
            input('')
    finally:
        session.close()

def insert_prof(obj: Professor) -> None:
    query = text("""
        INSERT INTO professores (nome, idade, cpf, telefone, sexo, formacao, valorHora)
        VALUES (:nome, :idade, :cpf, :telefone, :sexo, :formacao, :valorHora)
    """)
    session = db_connect()
    try:
        session.execute(query, obj.__dict__)
        session.commit()
        print('Registro inserido com sucesso!')
        input('')
    except Exception as error:
        session.rollback()
        raise Exception('Deu ruim')
    finally:
        session.close()

def insert_aluno(obj: Aluno) -> None:
    query = text("""
        INSERT INTO alunos (nome, idade, cpf, telefone, sexo, matricula, turma)
        VALUES (:nome, :idade, :cpf, :telefone, :sexo, :matricula, :turma)
    """)
    session = db_connect()
    try:
        session.execute(query, obj.__dict__)
        session.commit()
        print('Registro inserido com sucesso!')
        os.system('pause') or None
    except Exception as error:
        session.rollback()
        raise Exception('Deu ruim')
    finally:
        session.close()

def excluir_registro(param: str, cpf: str) -> None:
    query = text("DELETE FROM " + param + " WHERE cpf = :cpf")
    session = db_connect()
    try:
        session.execute(query, {"cpf": cpf})
        session.commit()
        print('Registro deletado com sucesso!')
        os.system('pause') or None
    except Exception as error:
        session.rollback()
        raise Exception('Deu ruim')
    finally:
        session.close()

def updateAluno(obj: Aluno, cpf: str) -> None:
    query = text("""
        UPDATE alunos SET 
            nome = :nome,
            idade = :idade,
            cpf = :cpf,
            telefone = :telefone,
            sexo = :sexo,
            matricula = :matricula,
            turma = :turma
        WHERE cpf = :cpf_filter
    """)
    session = db_connect()
    try:
        session.execute(query, {**obj.__dict__, "cpf_filter": cpf})
        session.commit()
        print('Registro atualizado com sucesso!')
        os.system('pause') or None
    except Exception as error:
        session.rollback()
        raise Exception('Deu ruim')
    finally:
        session.close()

def updateProfessor(obj: Professor, cpf: str) -> None:
    query = text("""
        UPDATE professores SET 
            nome = :nome,
            idade = :idade,
            cpf = :cpf,
            telefone = :telefone,
            sexo = :sexo,
            formacao = :formacao,
            valorHora = :valorHora
        WHERE cpf = :cpf_filter
    """)
    session = db_connect()
    try:
        session.execute(query, {**obj.__dict__, "cpf_filter": cpf})
        session.commit()
        print('Registro atualizado com sucesso!')
        os.system('pause') or None
    except Exception as error:
        session.rollback()
        raise Exception('Deu ruim')
    finally:
        session.close()
