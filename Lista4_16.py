possiveis_salarios = [
    [200,299],[300,399],[400,499],
    [500,599],[600,699], [700,799],
    [800,899],[900,999]
    ]
quantidades = [0,0,0,0,0,0,0,0,0]

salarios = []
vendas_brutas = True
while vendas_brutas != 0:
    vendas_brutas = float(input("Digite a valor das vendas: "))
    if vendas_brutas == 0:
        break
    else:
        salario = (vendas_brutas * 0.09) + 200
        if salario < 1000:
            for i in range(len(possiveis_salarios)):
                if salario > possiveis_salarios[i][0] and salario < possiveis_salarios[i][1]:
                    quantidades[i] += 1
        else:
            quantidades[8] += 1
print("\n" * 3)
for i in range(len(possiveis_salarios)):
    print("Entre R$", possiveis_salarios[i][0], "e R$", possiveis_salarios[i]
[1], ":", quantidades[i])
print("Salarios maiores que R$1000:", quantidades[8])
