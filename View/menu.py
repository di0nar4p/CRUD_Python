from Controller.requisicoes import select_all,select_cpf,insert_prof,insert_aluno,excluir_registro,updateAluno,updateProfessor
from Models.aluno import Aluno
from Models.professor import Professor
import os

# Menu principal
def menu():
    while True:
        os.system('clear')or None
        op= int(input('''Selecione uma operação: 
                        1- Consultar. 
                        2- Inserir.
                        3- Deletar.
                        4- Atualizar.
                        0- Sair.
                         
                         '''))
        match op:
            case 1:
                os.system('clear')or None
                consulta= int(input('''                      
                1- Consultar alunos
                2- Consultar professores                
                0- Sair       
                      '''))
                
                
                
                if consulta==1:
                    os.system('clear')or None
                    busca= int(input('''
                    1- Consultar todos
                    2- Consultar por CPF
                    0- Sair     
                    '''))
                    
                    if busca == 1:
                        os.system('clear')or None
                        select_all('alunos')
                    elif busca == 2:
                        os.system('clear')or None
                        cpf= str(input('Digite o CPF do aluno: '))
                        select_cpf('alunos',cpf)
                    elif busca == 0:
                        break
                    
                if consulta==2:
                    
                    os.system('clear')or None
                    busca= int(input('''
                    1- Consultar todos
                    2- Consultar por CPF
                    0- Sair     
                    '''))
                    
                    if busca == 1:
                        os.system('clear')or None
                        select_all('professores')
                    if busca == 2:
                        os.system('clear')or None
                        cpf= str(input('Digite o CPF do professor: '))
                        select_cpf('professores',cpf)
                         
                
                elif consulta==0:
                    break
           
            case 2:
                os.system('clear')or None
                insercao= int(input('''                      
                1- Inserir aluno.
                2- Inserir professor.                
                0- Sair.       
                      '''))
                
                if insercao == 1:
                    os.system('clear')or None
                    nome=str(input('Nome: '))
                    idade=int(input('Idade: '))
                    cpf=str(input('CPF: '))
                    tel= str(input('Telefone: '))
                    sexo=str(input('Sexo: '))
                    matricula=str(input('Matricula: '))
                    turma=str(input('Turma: '))
                    aluno = Aluno(nome,idade,cpf,tel,sexo,matricula,turma)
                    insert_aluno(aluno)
                
                
                if insercao == 2:
                    os.system('clear')or None
                    nome=str(input('Nome: '))
                    idade=int(input('Idade: '))
                    cpf=str(input('CPF: '))
                    tel= str(input('Telefone: '))
                    sexo=str(input('Sexo: '))
                    formacao=str(input('Formação: '))
                    valHora=float(input('Valor hora: '))
                    prof=Professor(nome,idade,cpf,tel,sexo,formacao,valHora)
                    insert_prof(prof)
            case 3:
                os.system('clear')or None
                op= int(input('''                      
                1- Deletar aluno.
                2- Deletar professor.                
                0- Sair.       
                      '''))
                if op == 1:
                    cpf=input('Digite o CPF do aluno')
                    excluir_registro('alunos',cpf)
                elif op == 2:
                    cpf=input('Digite o CPF do professor')
                    excluir_registro('professores',cpf)
                elif op == 0:
                    break
            
            case 4:
                os.system('clear')or None
                op= int(input('''                      
                1- Atualizar aluno.
                2- Atualizar professor.                
                0- Sair.       
                      '''))
                if op == 1:
                    os.system('clear')or None
                    nome=str(input('Nome: '))
                    idade=int(input('Idade: '))
                    cpf=str(input('CPF: '))
                    tel= str(input('Telefone: '))
                    sexo=str(input('Sexo: '))
                    matricula=str(input('Matricula: '))
                    turma=str(input('Turma: '))
                    aluno = Aluno(nome,idade,cpf,tel,sexo,matricula,turma)
                    updateAluno(aluno,cpf)
                elif op == 2:
                    os.system('clear')or None
                    nome= str(input('Nome: '))
                    idade =int(input('Idade: '))
                    cpf= str(input('CPF: '))
                    tel= str(input('Telefone: '))
                    sexo= str(input('Sexo: '))
                    formacao= str(input('Formação: '))
                    valorHora= str(input('Valor hora: '))
                    professor = Professor(nome,idade,cpf,tel,sexo,formacao,valorHora)
                    updateProfessor(professor,cpf)
                elif op == 0:
                    break
                              
            
            case 0:
                break  
            
            
