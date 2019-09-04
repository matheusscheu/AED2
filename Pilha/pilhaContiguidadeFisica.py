class Nodo:
    def __init__(self):
        self.info = None

class pilha:
    def __init__(self,maximo):
        self.elemento = [0]*maximo
        self.base = 0
        self.limite = maximo
        self.topo = self.base -1
    
    def empilha(self,valor):
        if self.topo < self.limite:
            self.topo += 1
            self.elemento[self.topo] = valor
        else:
            print('Não é possivel')    
    
    def desempilha(self,valor):
        if self.topo >= self.base:
            self.topo -= 1
            aux = self.elemento[self.topo]
        
        return aux     

    def consulta(self):
        if self.topo >= self.base:
            return self.elemento[self.topo]
        else:
            print('Não é possivel realizar')

    def destroi(self):
        self.base = -1
        self.limite = -1
        self.topo = -1        

pi = pilha(10)
print(pi.elemento)
pi.empilha(1)
print(pi.elemento)
pi.empilha(2)
print(pi.elemento)
pi.empilha(3)
print(pi.elemento)
pi.desempilha(2)
print(pi.elemento)
print(pi.consulta())