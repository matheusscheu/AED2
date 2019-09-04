from conta import Conta

conta1 = Conta('matheus',50,21,300)

print(conta1.nome)
conta1.depositar(300)
print(conta1.saldo)
conta1.consulta()

conta1.sacar(100)

conta1.consulta()

