class Node:
    def __init__(self, valor, anterior = None, proximo = None):
        self.valor = valor     #o dado a ser utilizado
        self.prox = proximo    #o proximo nó
        self.ant = anterior    # o nó anterior

class LinkedDoubleList():
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, valor):
        #Insere quando a lista não esta vazia
        if self.head:  
            ponteiro = self.head
            while (ponteiro.prox):
                ponteiro = ponteiro.prox
            ponteiro.prox = Node(valor, ponteiro)
        else:
            #Insere quando a lista esta vazia
            self.head = Node(valor)

        self._size += 1

    #retorna a quantidade
    def __len__(self):
        return self._size

    #Inserir valores
    def insert(self, valor, pos):
        if pos > self._size or pos < 0:
            raise IndexError("list index out of range")
        elif pos == 0:
            self.head = Node(valor, None, self.head)
            if (self.head.prox != None):
                self.head.prox.ant = self.head
        else:
            ponteiro = self.head
            for i in range(1, pos):
                ponteiro = ponteiro.prox
            ponteiro.prox = Node(valor, ponteiro, ponteiro.prox)
            ponteiro.prox.ant = ponteiro
        self._size += 1

    #Remocao de valores
    def remove(self, pos):
        valor = 0
        if pos > self._size or pos < 0:
            raise IndexError("list index out of range")
        elif pos == 0:
            valor = self.head.valor
            self.head = self.head.prox
        self._size -= 1
        return valor

    def posFim(self, valor):
        ponteiro = self.head
        while (ponteiro.prox):
            ponteiro = ponteiro.prox
        i = -1
        while (ponteiro.ant):
            if ponteiro.valor == valor:
                return i
            ponteiro = ponteiro.ant
            i -= 1
        raise ValueError("{} não esta na lista".format(valor))
        
    def valorFim(self, pos):
        if pos < 0 or pos > self._size:
            raise IndexError("list index out of range")
        else:
            ponteiro = self.head
            while (ponteiro.prox):
                ponteiro = ponteiro.prox
            for i in range(1,pos):
                ponteiro = ponteiro.ant
            return ponteiro.valor

    def __str__(self):
        if (self.head):
            r = "["
            ponteiro = self.head
            while (ponteiro.prox):
                r += str(ponteiro.valor) + ','
                ponteiro = ponteiro.prox
            r += str(ponteiro.valor) + "]" 
            return r
        else:
            return "[]"

    def destroi(self):
        self.head = None

    
a = LinkedDoubleList()
a.append(4)
a.append(25)
a.append(7)
a.append(2)
a.append(9)
a.insert(88, 3)
print(len(a))
print(a)
a.remove(0)
print(a)
print(len(a))
print(a.posFim(2))
print(a.valorFim(1))
a.destroi()
print(a)