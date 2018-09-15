A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados = []
contador = 0
for i in range(len(A)):
    quadrados.append(A[contador] * A[contador])
    contador += 1
print("\nSoma dos quadrados: ", sum(quadrados))
