alturas = []
idades = []
alunos13 = []
baixo_media = []
n_aluno = 1
for i in range(30):
    print("\nAluno n°", n_aluno)
    altura = alturas.append(float(input("Digite a sua altura: ")))
    idade = int(input("Digite a sua idade: "))
    if idade > 13:
        alunos13.append(idade)
    idades.append(idade)
    n_aluno += 1

media = sum(alturas) / len(alturas)
contador = 0
for i in range(len(alunos13)):
    if alunos13[contador] < media:
        baixo_media.append(alunos13[contador])
    contador += 1

print("Alunos com mais de 13 anos possuem altura inferior à média: "len(baixo_media))
