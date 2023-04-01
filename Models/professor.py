from Models.pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self,nome:str, idade:int,cpf:str,telefone:int,sexo:str, formacao:str, valorHora:float) -> None:
        super().__init__(nome,idade,cpf,telefone,sexo)
        self.formacao = formacao
        self.valorHora = valorHora
        
    #retorna formação
    @property
    def getFormacao(self):
        return self.formacao
    #seta formação
    def setFormacao(self,formacao):
        self.formacao= formacao
    
    #retorna valor hora
    @property
    def getValorHora(self):
        return self.valorHora
    
    #seta valor hora
    def setValorHora(self,valorHora):
        self.valorHora = valorHora
    
