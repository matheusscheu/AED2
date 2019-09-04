class Node:
    def __init__(self, valor, proximo):
        self.valor = valor     #o dado a ser utilizado
        self.prox = proximo     #o proximo nó

class LinkedList:
    def __init__(self):
        self.head = None
        self.cont = 0
   
    # busca por um valor e retorna o índice 
    def busca(self, a):
        node = self.head
        posicao = 0
        if node == None:
            print("Lista vazia!")
            return -1
        else:
            while node != None:
                if(node.valor == a):
                    return posicao
                else:
                    posicao += 1
                    continue
            return -1

    # em uma determinada posição insere um valor na lista
    def insere(self, posit,value):
        if(posit < 0 or posit > self.cont):
            return False
        elif posit == 0 and self.cont == 0:
            self.head = Node(value, None)
            self.cont += 1
        else:
            nodeAtu = self.head
            for i in range(1,posit):
                nodeAtu = nodeAtu.prox
            nodeAtu.prox = Node(value, nodeAtu.prox)
        self.cont+=1
        return self

    # em uma determinada posição remove da lista
    def remove(self, pos):
        if pos < 0 or pos >= self.cont:
            return None
        elif pos == 0:
            remover = self.head.valor
            self.head = self.head.prox
            self.cont -= 1
            return remover
        else:
            nodeAtu = self.head
            for i in range(1, pos):
                nodeAtu = nodeAtu.prox
            remover = nodeAtu.prox
            nodeAtu.prox = nodeAtu.prox.prox
            self.cont -= 1
            return remover
    
    
     # imprime na sequência
    def imprime(self):
        node = self.head
        if node == None:
            print("Esta lista está vazia")
        else:
            while node != None:
                print(node.valor, end=", ")
                node = node.prox
        print()

    # retorna número de elementos 
    def __len__(self):
        return self.cont -1

    # compara as listas para verificar se são iguais 
    
    def comparaListas(self,l2):
        n1 = self.head
        n2 = l2.head
        if self.cont != l2.cont:
            return False
        while(n1):
            if n1.valor != n2.valor:
                return False
            n1 = n1.prox
            n2 = n2.prox
        return True
    
    # return da lista invertida
    def reverse(self):
        if(self.head != None):
            r = []
            valor = self.head
            while(valor != None):
                r.append(valor.valor)
                valor = valor.prox
            return r[::-1]

    # Implemente um algoritmo que receba como parâmetro o endereço do primeiro elemento de uma lista encadeada de inteiros. 
    # Deve ser impresso na tela uma lista de pares (posição, valor) 
    # onde o valor é maior que a média de todos os valores contidos na lista.
    
    def mediaMaior(self):
        inicio = self.head
        media = 0
        r = ''
        while inicio:
            media += inicio.valor
            inicio = inicio.prox
        media = media / self.cont
        inicio = self.head
        cont = 0
        while inicio:
            if inicio.valor > media:
                r += "({} , {})".format(inicio.valor,cont)
            inicio = inicio.prox
            cont += 1        
        return r    

               
#criando duas listas com 5 valores cada
primLista = LinkedList()
for i in range(0,5):
    primLista.insere(i,i+1)

segundalista = LinkedList()
for i in range(0,5):
    segundalista.insere(i,i+2)

# impressão da primeira lista 
print('Lista: ', end='')
primLista.imprime()

print('Tamanho da lista:', len(primLista))

# impressão da primeira lista inversamente
print('lista inversa:',primLista.reverse())

# comparação de duas listas
print('Comparando as duas listas :{}'.format(primLista.comparaListas(segundalista)))

# Retorna os valores maiores que a média

print('Valores maiores que a média:',primLista.mediaMaior())