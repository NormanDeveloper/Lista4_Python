import random
numeros = []
par = []
impar = []


for i in range(20):
    numero_aleatorio = numeros.append(random.randrange(0, 100))

count = 0
for i in range(20):
    if numeros[count] % 2 == 0:
        par.append(numeros[count])
    else:
        impar.append(numeros[count])
    count += 1

print("\nNumeros: ", numeros, "\nPares: ", par, "\nImpares: ", impar)
