from functools import reduce
numeros = [1, 2, 3, 4, 5]
multiplicados = reduce((lambda x, y: x * y), numeros)
print("\nSoma: ", sum(numeros), "\nMultiplicão: ", multiplicados, "\nNúmeros: ", numeros)
