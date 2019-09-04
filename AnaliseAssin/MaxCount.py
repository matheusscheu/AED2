def maxcount(A):                        
    maxx = A[0]
    count = 0
    n = len(A)
    for i in range(n):
        maxx = A[i]
    for i in range(n):
        count += A[i]
        for j in range(n - 1):
            A[i] = A[i] + (maxx)

#   Custo      | Número de interações
#     c2       |        1
#     c3       |        1
#     c4       |        1
#     c5       |        n+1
#     c6       |        n
#     c7       |        n+1
#     c8       |        n
#     c9       |        n(n + 1 - 1) = n²
#     c10       |        n² - 1

#T(n) = c2+c3+c4+c5(n+1)+c6*n+c7(n+1)+c8*n+c9*n²+c10(n²-1)
#T(n) = 1+1+1 + n +1 + n + n+ 1 + n + n² + n² -1
#T(n) = 4 + 4n + 2n²

#   Definição theta
#   c1*n² <= 4n + 2n² <= c2*n²
#   Divide tudo por n²
#   c1 <= 4/n + 2 <= c2     valido para todo n<= 1 logo n0  = 1

#   c2 se considera o n = 1 logo:
#   4+ 2 <= c2 logo c2 =  6

#   c1 para o c1 aplicamos o limite n tendendo a infinito logo:
#   lim    4/n + 2 = 2      logo c1 = 2
#   n->infinito

# R: 2n² <= 4n + 2n² <= 6n²

#c2 = 2 | c3 = 1 | c4 = 4 |c5 = 3 | c6 = 2 | c7 = 3 | c8 = 3 | c9 = 3 | c10 = 5
#t(n) = 2+1+4+3(n+1)+2n+3(n+1)+3n+3n²+5(n²-1)
#t(n) = 7 + 3n + 3 + 2n + 3n + 3 + 3n + 3n² + 5n² -5
#t(n) = 8 + 11n + 8n²

#Definição theta
#   c1*n2 <= 11n + 8n² <= c2n²
#   Divide tudo por n²
#   c1 <= 11/n + 8 <= c2    valido para todo n <=1 logo n0 = 1

#   c2 se considera o n = 1 logo:
#   11+ 8 <= c2 logo c2 = 19

#   c1 para o c1 aplicamos o limite n tendendo a infinito logo:
#   lim    11/n + 8 = 8      logo c1 = 8
#   n->infinito

# R: 8n² <= 11n + 8n² <= 19n²