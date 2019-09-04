def selectionSort(A):
    n = len(A)
    for j in range(n - 1):
        smallest = j
        for i in range(j+1, n):
            if A[i] < A[smallest]:
                smallest = i
        tmp = A[j]
        A[j] = A[smallest]
        A[smallest] = tmp

#   Custo      | Número de interações
#     c2       |        1
#     c3       |        n
#     c4       |        n-1
#     c5       |        (n-1)
#     c6       |        t6
#     c7       |        t6-1
#     c8       |        (n-1)
#     c9       |        (n-1)
#     c10       |        (n-1)

#     t6 pior caso
#   S(n-j+1) = (n(n-1))/2
#            = (n² -n )/2
#            = n²/2 - n/2

#   T(n) = c2 + c3n + c4(n-1) + c5(n-1) c6(n²/2 - n/2) + c7(n²/2 - n/2 -1) + c8(n-1) + c9(n-1) + c10(n-1)

#     t6 melhor caso
#   S (1) = n - 1

#   T(n) = c2 + c3n + c4(n-1) + c5(n-1) c6(n-1) + c7(n-2) + c8(n-1) + c9(n-1) + c10(n-1)

# Notação theta

# c1n² <= n²/2 - n/2 <= c2n²
# Divide tudo por n²
# c1<= 1/2 - 1/2n <= c2

# 1/2 - 1/2n <= c2  usamos aqui o maior valor positivo logo c2 = 1/2 todo n<=1

# c1<= 1/2 - 1/2n   n = 1 é o primeiro n logo pegamos o proximo valor
# c1<= 1/2 - 1/4
# c1<= (2 -1)/4
# c1<= 1/4          logo c1 = 1/4

#R: n²/4 <= n²/2 - n/2 <= n/2