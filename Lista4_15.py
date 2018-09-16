notas = []
acima_media = []
abaixo7 = []
nota = True
while nota != -1:
    nota = float(input("Digite a nota: "))
    if nota == -1:
        break
    else:
        notas.append(nota)
print("\nValores lidos: ", len(notas))
print("Valores na ordem: ", notas)
notas.reverse()
for i in range(len(notas)):
    print(notas[i])
print("Soma dos valores: ", sum(notas))
media = sum(notas) / len(notas)
print("Media dos valores: ", media)

for i in range(len(notas)):
    if notas[i] > media:
        acima_media.append(notas[i])
print("Quantidade de valores a cima da media: ", len(acima_media))
for i in range(len(notas)):
    if notas[i] < 7:
        abaixo7.append(notas[i])
print("Quantidade de notas a baixo de 7: ", len(abaixo7))
print("Fim do programa. Thau")