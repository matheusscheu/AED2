class Node:
  def __init__(self,data,prox= None):
    self.data = data
    self.prox = prox

class Lista:
  def __init__(self,data,prox= None):
    self.data = data
    self.prox = prox
    
  def imprime(self):
    nodo = self.ini
    if nodo == None:
      print("Lista vazia")
    else:
      while nodo != None:
        print(nodo.value)
        nodo = nodo.next
      
  def busca(self,valor):
    nodo = self.ini
    pos = 0
    while nodo != None:
      if nodo.valor == valor:
        return pos
      pos +=1
      nodo=nodo.prox
    return -1 

  def insere(self, valor,pos): 
    if pos < 0 or pos > self.cont:
      return False
    elif pos == 0                  #insere no inicio
      self.ini = Nodo(valor,None)
    else:
      nodo_atual = self.ini         #insere outros casos
      for i in range(1,pos):
        nodo_atual = nodo_atual.prox
      nodo_atual.prox = Nodo(nodo_atual.prox)
    self.count += 1
    return True      

  def remove(self, pos):
    if pos < o or pos >= self.cont:
      return None
    elif pos == 0:
      remover - self.ini.prox
      self.cont -= 1
      return remover  