class Fila:
    def __init__(self, maxx):
        self.limit = maxx
        self.elementos = [0] * maxx
        self.ini = -1
        self.end = -1
        self._size = 0
        self.offset = -1
        
    def __len__(self):
        return self._size

    def insert(self, elem):
        if ((self._size) >= self.limit) or (self.ini - self.end - 1 == 0):
            raise IndexError("Fila cheia!!")
        else:
            if (self.ini < 0):
                self.ini = 0
                self.end = 0
                self.offset = 0
            elif (self.end < self.limit):
                self.end += 1
                self.offset = self.end
                if (self.offset > self.limit - 1):
                    self.offset = 0
                    self.end = self.offset
            else:
                self.offset += 1
                self.end = self.offset
            self._size += 1
            self.elementos[self.offset] = elem

    def remove(self):
        if (self._size <=0):
            print("Lista vazia")
        else:
            if (self.ini <= self.limit - 1):
                data = self.elementos[self.ini]
                self.elementos[self.ini] = 0
                self.ini += 1
            else:
                data = self.elementos[self.ini]
                self.ini = 0
            self._size -=1
            return data

    def consult(self):
        if (self._size > 0):
            return self.elementos[self.ini]

    def destroi(self):
        self.elementos = [0] * self.limit
        self.ini = -1
        self.end = -1
        self._size = 0
        self.offset = -1

f = Fila(3)
f.insert(23)
f.insert(80)
f.insert(10)
f.insert(10)