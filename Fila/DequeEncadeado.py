from NodeB import Node

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def insertIni(self,data):
        node = Node(data)
        if (self.tail == None):
            self.tail = node
        else:
            self.tail.ant = node
            self.tail = node
        if self.head == None:
            self.head = node

        self._size +=1

    def insertEnd(self, data):
        node = Node(data)
        if (self.tail == None):
            self.tail = node
        else:
            self.head.ant = node
            self.head = node
        if self.tail == None:
            self.tail = node
                
        self._size +=1
    
    def removeIni(self):
        if self._size > 0:
            elem = self.head.data
            self.head = self.head.ant
            self._size -= 1
            return elem
        else:
            print ("fila vazia.")

    def removeEnd(self):
        if self._size > 0:
            elem = self.tail.data
            self.tail = self.tail.ant
            self._size -= 1
            return elem
        else:
            print ("fila vazia.")

    def consultIni(self):
        #retorna o topo sem remover
        if self.head != None:
            elem = self.head.data
            return elem
        else:
            print ("fila vazia.")
    
    def consultEnd(self):
        #retorna o fim sem remover
        if self.tail != None:
            elem = self.tail.data
            return elem
        else:
            print ("fila vazia.")        
    
    def destroi(self):
        self.ini = -1
        self.end = -1
        self._size = 0

    def __repr__(self):
        r = '['
        pointer = self.head
        while (pointer):
            r = r + str(pointer.data) + ','
            pointer = pointer.next
        return r + ']'

    def __str__(self):
        return self.__repr__()    
        
        

f = Deque()
f.insertIni(5)
f.insertIni(4)
f.insertIni(9)

f.removeIni()
print(len(f))

f.insertEnd(6)
f.insertEnd(1)
f.insertEnd(3)
f.removeEnd()
print(len(f))

f.consultEnd()
f.consultIni()


f.destroi()
print(len(f))
