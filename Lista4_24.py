import random
lancamentos = []
for i in range(100):
    lancamentos.append(random.randrange(1, 6 + 1))
for i in range(6):
    print("O número", i + 1, "foi gerado ", lancamentos.count(i + 1), "vezes")