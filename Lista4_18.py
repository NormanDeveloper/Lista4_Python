votos = []
votos_jogadores_votados = []
numeros_jogadores_votados = []
voto = True
n_voto = 1
while voto != 0:
    print("Voto n°", n_voto)
    voto = int(input("Digite o número do jogador: "))
    if voto == 0:
        break
    else:
        while voto > 23 or voto < 1:
            print("[Voto inválido.]")
            print("Voto n°", n_voto)
            voto = int(input("Digite novamente: "))
        votos.append(voto)
    n_voto += 1
print("\nTotal de votos: ", len(votos))
contador = 1
for i in range(23):
    if contador not in votos:
        contador += 1
        continue
    else:
        votos_jogadores_votados.append(votos.count(contador))
        numeros_jogadores_votados.append(contador)
        print("\nVotos para o jogador camisa n°", contador, " = ", votos.count(contador))
        print("Percentual de votos: ", round(100 * votos.count(contador) / len(votos), 2), "%")
        contador += 1
melhor = votos_jogadores_votados.index(max(votos_jogadores_votados))
print("\nO jogador mais votado foi o n°", numeros_jogadores_votados[melhor], "com ", votos_jogadores_votados[melhor], "votos")
print("Ganhou com", round(100 * votos_jogadores_votados[melhor] / len(votos), 2), "% dos votos")