class Carro:
    def __init__(self,placa,marca,modelo,ano):
    def getChave(self):
class Tabela:
    def busca(self,chave):
        for i in range(0,self.n):
            if self.tab[i].getChave() == chave
                return i
        print("Não encontrado")
        return -1
    def insere(self,chave):
        if self.cheia():
            print("tabela cheia")
            return   
        pos = self.busca(item.getChave())
        if pos >=0:
            self.tab[pos] = item
        else:
            self.tab[self]    

    def apaga(self,chave): 
        pos = self.busca(chave)
        if pos != 1:
            for i in range(pos,self.n-1):
                self.tab[i] = self.tab[i+1]  
            print("Foi apagado")
            self.n                     