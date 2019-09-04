class Aluno:
  def __init__(self, nome, matr, nasc):
    self.nome = nome
    self.matr = matr
    self.nasc = nasc
  def procurar(self):
    return ('nome: '+ str(self.nome) + ' - matricula: ' + str(self.matr) + ' - data de nascimento: ' +str(self.nasc))
  
  def procurarNome(self):
    return self.nome
    
  def procurarMatricula(self):
    return self.matricula
  
  def __del__(self):
    return "deletado"

    
#a = Aluno('joao', 126717, '08/09/1999')
#print(joao.procurar())

lista=[]
lista.append(Aluno('Maria', 121212, '11/05/2000'))
lista.append(Aluno('Joao', 131313, '25/010/1998'))
lista.append(Aluno('Caio', 141414, '05/04/1997'))
lista.append(Aluno('Pablo', 151515, '12/05/1999'))

#printa o nome que esta na posicao da lista
#print(lista[0].procurarNome())


# procura um nome, se encontrar ele printa todos os dados
cont = 0
encontrou = False
nome = input()
for i in lista:
  if i.procurarNome() == str(nome):
    encontrou = True
    print(lista[cont].procurar())
  cont +=1
if not encontrou:
  print("nome nao encontrado!")
    