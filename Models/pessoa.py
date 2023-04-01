class Pessoa():
    def __init__(self, nome:str, idade:int,cpf:str,telefone:int,sexo:str)-> None:
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefone = telefone
        self.sexo = sexo
        
        
    #retorna nome
    @property
    def getNome(self):
        return self.nome
    
    #seta nome
    def setNome(self, nome):
        self.nome= nome
    
    
    #retorna idade
    @property
    def getIdade(self):
        return self.idade
    
    #seta idade
    def setIdade(self, idade):
        self.idade = idade
    
    #retorna cpf
    @property
    def getCpf(self):
        return self.sexo
    
    #seta cpf
    def setCpf(self, cpf):
        self.cpf = cpf  
  
    #retorna telefone
    @property
    def getTelefone(self):
        return self.telefone
    
    #seta telefone
    def setTelefone(self, telefone):
        self.telefone = telefone
    
    #retorna sexo
    @property
    def getSexo(self):
        return self.sexo
    
    #seta sexo
    def setSexo(self,sexo):
        self.sexo = sexo