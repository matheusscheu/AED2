class Data:
  def __init__(self, data, dia, mes, ano, dias):
    self.dia = dia
    self.mes = mes
    self.ano = ano
    self.data = data
    self.dias = dias
    
  def inicializaData(self):
    if self.ano > 100 and self.ano < 2100:
      if self.mes >= 1 or self.mes <=12:
        if self.mes == 2 and self.dia <= 28:
          if self.dia <= 31:
            return True
    return False
  
  def acrescentaDia(data,dias):
    x =self.data.split('/')
    x[0] = dia
    x[1] = mes
    x[2] = ano
    
    print(dia, mes, ano)
   
a = Data('02/03/2019',28 , 5, 2019, 20)
print(a.inicializaData())
