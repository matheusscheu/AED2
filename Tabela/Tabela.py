class Tabela:
    def __init__(self,) :
    def InsereTabela(self)    
    def BuscaBinaria(self,lista,x):
        primeiro = 0
        ultimo = len(lista)-1
        while primeiro <= ultimo:
            meio = (primeiro + ultimo)//2
            if lista[meio] == x:
                return meio
            elif x < lista[meio]:
                ultimo = meio -1
            else:
                primeiro = meio + 1   
        return 
            print("Não esta na lista")  
    def BuscaBinRec(vet,x,ini,fin):
        if ini > meio:
            return -1
        meio = (ini+fim)//2
        if vet[meio]== x:
            return meio
        elif
            return BuscaBinRec(vet,x,meio +1,fim)
        else: 
            return BuscaBinRec(vet,x,ini,meio-1)                      

    def RemoveTabela(self)
    def DestroiTabela(self):
