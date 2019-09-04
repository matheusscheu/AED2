class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

# inserir na fila
# remover da fila
# consultar o primeiro elemento da fila     
   
class Fila:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def inserirF(self, elem):
        #insere um elem na frente da fila
        node = Node(elem)
        if self.last == None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first == None:
            self.first = node
        
        self.size = self.size + 1



    def inserirA(self, elem):
        #insere um elem atrás da fila
        node = Node(elem)
        if self.last == None:
            self.last = node
        else:
            self.first.back = node
            self.first = node
        
        if self.last == None:
            self.last = node
        
        self.size = self.size + 1



    def removerF(self):
        #remove o elemento da frente da fila
        if self.size > 0:
            elem = self.first.data
            self.first = self.first.next
            self.size -= 1
            return elem
        else:
            print ("fila vazia.")

    def removerA(self):
        #remove o elemento atrás da fila
        if self.size > 0:
            elem = self.last.data
            self.last = self.last.next
            self.size -= 1
            return elem
        else:
            print ("fila vazia.")

    def consultar(self):
        #retorna o topo sem remover
        if self.first != None:
            elem = self.first.data
            return elem
        else:
            print ("fila vazia.")

    def destruir(self):
        #destrói a fila
        self.first = None
        self.last = None
        self.data = None