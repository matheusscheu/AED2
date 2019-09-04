from node import Node

class Pilha:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -=1
            return node.data
        raise IndexError("A pilha est? vazia")

    def peek(self):
        if self._size > 0:
            return self.top.data
        raise IndexError("A pilha est? vazia")

    def equal(self, p):
        point = self.top
        point2 = p.top
        while (point.next):
            if point.data != point2.data:
                return False
            point = point.next
            point2 = point2.next
        return True

    def __len__(self):
        return self._size

    def __repr__(self):
        r = ''
        pointer = self.top
        while (pointer):
            r = r + str(pointer.data) + '\n'
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()