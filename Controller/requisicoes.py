from Controller.conexao import db_connect
from Models.professor import Professor
from Models.aluno import Aluno
import os

#NO FUTURO RETORNARÁ UM JSON PARA QUEM ESTIVER FAZENDO A REQUISIÇÃO


#retorna todos os valores de alunos ou professores
def select_all(param:str)-> None:

    '''RETORNA TODOS OS VALORES DE QUALQUER TABELA'''
    query = f'''SELECT * FROM {param}'''
    conn = db_connect()
    cursor = conn.cursor()

    cursor.execute(query)
    registros = cursor.fetchall()
    for row in registros:
        print(row)
    input('')  

#retorna o aluno ou professor por cpf
def select_cpf(param:str, cpf:str)-> None:
    '''RETORNA DADOS FILTRADOS POR CPF'''
    query= f'''SELECT * FROM {param} WHERE cpf= {cpf}'''
    conn = db_connect()
    cursor = conn.cursor()

    cursor.execute(query)
    registro = cursor.fetchall()
    for row in registro:
        print(row)
    input('')      
    
    
#insere um professor no banco 
def insert_prof(obj:Professor)-> None:
    query= f'''INSERT INTO professores (nome, idade, cpf, telefone, sexo, formacao, valorHora)
    VALUES(
            "{obj.nome}",
            "{obj.idade}",
            "{obj.cpf}",
            "{obj.telefone}",
            "{obj.sexo}",
            "{obj.formacao}",
            "{obj.valorHora}")'''
    conn = db_connect()
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        conn.commit()
        print('Registro inserido com sucesso!')
        input('')  
        
    except Exception as error:
        raise error('Deu ruim')
    else:
        pass


#insere um aluno no banco    
def insert_aluno(obj:Aluno)-> None:
    query= f'''INSERT INTO alunos(nome,idade,cpf,telefone,sexo,matricula,turma)
    VALUES
    (
            "{obj.nome}",
            "{obj.idade}",
            "{obj.cpf}",
            "{obj.telefone}",
            "{obj.sexo}",
            "{obj.matricula}",
            "{obj.turma}")'''
    conn = db_connect()
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        conn.commit()
        print('Registro inserido com sucesso!')
        os.system('pause')or None
        
    except Exception as error:
        raise error('Deu ruim')
    else:
        pass
    
def excluir_registro(param:str,cpf:str)-> None:
    '''EXCLUI UM REGISTRO DO BANCO FILTRADO PELO CPF'''
    query= f'DELETE FROM {param} WHERE cpf={cpf}'
    conn = db_connect()
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        conn.commit()
        print('Registro deletado com sucesso!')
        os.system('pause')or None
        
    except Exception as error:
        raise error('Deu ruim')
    else:
        pass
    
def updateAluno(obj:Aluno,cpf:str)-> None:
    query= f'''UPDATE alunos SET 
            nome= "{obj.nome}",
            idade= "{obj.idade}",
            cpf= "{obj.cpf}",
            telefone= "{obj.telefone}",
            sexo= "{obj.sexo}",
            matricula= "{obj.matricula}",
            turma ="{obj.turma}"
            WHERE cpf={cpf}'''
    conn = db_connect()
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        conn.commit()
        print('Registro atualizado com sucesso!')
        os.system('pause')or None
        
    except Exception as error:
        raise error('Deu ruim')
    else:
        pass    


def updateProfessor(obj:Professor,cpf:str)-> None:
    query= f'''UPDATE professores SET 
            nome= "{obj.nome}",
            idade= "{obj.idade}",
            cpf= "{obj.cpf}",
            telefone= "{obj.telefone}",
            sexo= "{obj.sexo}",
            formacao= "{obj.formacao}",
            valorHora= "{obj.valorHora}"
            WHERE cpf={cpf}'''
    conn = db_connect()
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        conn.commit()
        print('Registro atualizado com sucesso!')
        os.system('pause')or None
        
    except Exception as error:
        raise error('Deu ruim')
    else:
        pass    
    