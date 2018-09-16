votos = []
numero_votos = []
opcoes = ['Windowns Server', 'Unix', 'Linux', 'NetWare', 'MacOS', 'Outro']
voto = True
n_voto = 1
while voto != 0:
    print("\nVoto n°", n_voto)
    voto = int(input("Digite o seu voto: "))
    if voto == 0:
        break
    else:
        while voto > 6 or voto < 1:
            print("[Voto invalido]")
            print("\nVoto n°", n_voto)
            voto = int(input("Digite o seu voto novamente: "))
        votos.append(voto)
    n_voto += 1

print_sistema = ("Sistema Operacional")
espaco1 = "      "
espaco2 = "   "
print_votos = "Votos"
print("\n" * 2)
print(print_sistema, espaco1, print_votos, " " * (len(espaco2) * 2), "%")
print("-" * len(print_sistema), espaco1, "-" * len(print_votos), espaco2, "-" * 7)
for i in range(len(opcoes)):
    numero_votos.append(votos.count(i + 1))
    print(opcoes[i], " " * (len(print_sistema) - len(opcoes[i]) + len(print_votos) + 3), votos.count(i + 1), " " * (len(espaco2) * 2), round(100 * votos.count(i + 1) / len(votos), 2), "%")
indice_ganhador = numero_votos.index(max(numero_votos))
print("\nO sistema mais votado foi o ", opcoes[indice_ganhador], " com ", numero_votos[indice_ganhador], " votos.")
print("Equivalente a ", round(100 * numero_votos[indice_ganhador] / len(votos), 2), "% dos votos.")
