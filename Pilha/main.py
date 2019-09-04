from pilha import Pilha

p = Pilha()
#print(p.peek())
p.push(5)
p.push(3)
p.pop()
print(p.peek())
p.pop()
p.push(9)
p.push(1)
print(p.peek())
p.push(4)
p.pop()
p.pop()

p1 = Pilha()
p1.push(1)
p1.push(2)
p1.push(3)

p2 = Pilha()
p2.push(1)
p2.push(3)
p2.push(3)

print(p1.equal(p2))