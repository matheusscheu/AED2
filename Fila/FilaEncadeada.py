from node import Node

class Fila:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def insert(self, data):
        node = Node(data)
        if (self.head == None):
            self.head = node
            self.tail = self.head
        else:
            self.fim.next = node
            self.fim=self.fim.prox
        self._size +=1

    def remove(self):
        if (self.head == None):
            return False
        else:
            data = self.head.data
            self.head = self.head.next
            self._size -=1
        return data

    def consult(self):
        if self.head == None:
            print("Lista vazia")
        else:
            return self.head.data


    def __repr__(self):
        r = '['
        pointer = self.head
        while (pointer):
            r = r + str(pointer.data) + ','
            pointer = pointer.next
        return r + ']'

    def __str__(self):
        return self.__repr__()