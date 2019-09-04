class Empregado:
  def __init__(self, nome, cpf, salario):
    self.nome = nome
    self.cpf = cpf
    self.salario = salario

  def verificar(self):
    return ('nome: '+ str(self.nome) + ' - CPF: ' + str(self.cpf) + ' - Salario: ' +str(self.salario))
  
  def procurarNome(self):
    return self.nome
    
  def procurarCPF(self):
    return self.cpf

  def procurarSalario(self):
    return self.salario
  
  def __del__(self):
    return "deletado"

lista=[]
lista.append(Empregado('Maria', 15151551, 15000))
lista.append(Empregado('Junior', 77751551, 50000))
lista.append(Empregado('Amelia', 12020251, 24000))
lista.append(Empregado('Renata', 17979791, 76000))
lista.append(Empregado('Rafael', 20202441, 15000))

def mediaSalario():
  total = 0
  for i in lista:
    total += float(i.procurarSalario())
    print(i.procurarSalario())
  media = total/len(lista)
  return media

del lista[2]

lista.append(Empregado('jocely', 45484551, 75000))

print(mediaSalario())
print(len(lista))    