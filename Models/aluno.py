from Models.pessoa import Pessoa
class Aluno(Pessoa):
    def __init__(self,nome:str,idade:int,cpf:str,telefone:int,sexo:str,matricula:str,turma:str ) -> None:
        super().__init__(nome,idade,cpf,telefone,sexo)
        
        self.matricula = matricula
        self.turma= turma
        
    #retorna matricula
    @property
    def getMatricula(self):
        return self.matricula
    
    #Seta matricula        
    def setMatricula(self,matricula):
        self.matricula = matricula
        