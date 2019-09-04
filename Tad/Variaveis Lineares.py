class Lista:
  def __init__(self, maxm):
    self.elemento= [0]*maxm
    self.ini = -1
    self.fim = -1
    
    
  def consulta(self,posicao):
    if posicao > (self.fim - self.ini) or posicao < 0:
      return False
    else:
      return self.elemento[self.ini + posicao]
    
    
  def consultaElemento(self,elemento):
    for i in range(self.ini,self.maxm):
      if self.elemento[i] == elemento:
        return i
    return -1   
  
  def insereEspecial(self,n1,n2):
    for i in range(self.ini,self.maxm):
      if self.elemento[i] == n1:
        self.insere(n2,i+1)
           
  
  
  def insere(self, elem, posicao):
    if (self.ini == -1 and posicao != 0) or (self.ini == 0 and self.fim == (maxm - 1)) or (posicao < 0) or (posicao> self.fim - self.ini + 1):
      return False
    else:
      if self.ini == -1:
        self.ini = 0
        self.fim = 0
      else:
        if self.fim != (maxm - 1):
          for i in range(self.fim, self.ini+posicao-1,-1):
            self.elemento[i+1] = self.elemento[i]
          self.fim += 1
        else:
          for i in range(self.ini,self.ini+posicao):
            self.elemento[i-1] = self.elemento[i]
          self.ini = self.ini-1  
      self.elemento[self.ini + posicao] = elem
      
      
      
      
  def remove(self,posicao):
    if((posicao> self.fim - self.ini) or (posicao < 0)):
      print("erro: posicao invalida")
    else:
      rem = self.elemento[self.ini+posicao]
      if(posicao - self.ini> self.fim -posicao):
        for i in range(self.ini + posicao, self.fim):
          self.elemento[i] = self.elemento[i+1]
        self.elemento[self.fim]=0
        self.fim = self.fim -1
      
      else:
        for i in range(self.ini + posicao, self.fim,-1):
          self.elemento[i] = self.elemento[i-1]
        self.elemento[self.fim]=0
        self.fim = self.fim + 1
      
      return rem
          
      
  def destroi(self):
    self.elemento = none
    self.ini = -1
    self.fim = -1

l = lista(10)    