class Calculadora:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def soma(self):
    return self.a + self.b
  
  def subtrai(self):
    return self.a - self.b
  
  def multiplica(self):
    return self.a * self.b
  
  def divide(self):
    return self.a / self.b

a = Calculadora(10,2)
print(a.soma())
print(a.subtrai())
print(a.multiplica())
print(a.divide())