A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
intercalada = []
contador = 0
for i in range(10):
    intercalada.append(A[contador])
    intercalada.append(B[contador])
    contador += 1
print(intercalada)
