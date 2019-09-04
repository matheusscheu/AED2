def __init__(self):
    
    self.init_vet = Init_vet
    self.fim_vet = Fim_vet
    self.init_list = Init_list
    self.fim_list = Fim_list
    self.maior = Maior
    self.menor= Menor
    
class Lista:
  def __init__(self, maxm):
    self.elemento= [0]*maxm
    self.ini = -1
    self.fim = -1    
  
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