class Conta:
    def __init__(self,nome,cpf,idade,saldo):
        self. nome = nome
        self.cpf = cpf
        self. idade = idade
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo = self.saldo + valor 

    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
        else:
            print("saldo insuficiente")

    def consulta(self):
        print('Nome do titular: ' + self.nome)
        print('CPF do titural: ' + str(self.cpf))
        print('Saldo atual: ' + str(self.saldo))       
    




