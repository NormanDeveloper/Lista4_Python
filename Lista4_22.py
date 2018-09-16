defeitos = ['necessita da esfera',
            'necessita de limpeza',
            'necessita troca do cabo ou conector',
            'quebrado ou inutilizado'
            ]
numeros_identificacao = []
numeros_defeitos = []
numero_identificacao = True
n_mouse = 1
while numero_identificacao != 0:
    print("\nMouse n°", n_mouse)
    numero_identificacao = int(input("Digite o número de identificação do mouse: "))
    if numero_identificacao == 0:
        break
    else:
        while numero_identificacao in numeros_identificacao:
            print("[Número repetido]")
            print("\nMouse n°", n_mouse)
            numero_identificacao = int(input("Digite o número de identificação do mouse: "))
        numero_defeito = int(input("Digite o número correspondente ao defeito: "))
        while numero_defeito > 4 or numero_defeito < 1:
            print("[Número invalido]")
            numero_defeito = int(input("Digite o número correspondente ao defeito: "))
        numeros_identificacao.append(numero_identificacao)
        numeros_defeitos.append(numero_defeito)
    n_mouse += 1
print("\nQuantidade de mouses: ", len(numeros_identificacao))
for i in range(len(defeitos)):
    print("Situação: ", defeitos[i], "/ Quantidade: ", numeros_defeitos.count(i + 1), "/ Porcentagem: ", round(100 * numeros_defeitos.count(i + 1) / len(numeros_identificacao), 2), "%")
