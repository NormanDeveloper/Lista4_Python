maior7 = []
n_aluno = 1
for i in range(10):
    notas = []
    print("\nAluno n°", n_aluno)
    for i in range(4):
        nota = notas.append(float(input("Digite a sua nota: ")))
        while nota > 10 or nota < 0:
            print("[nota ivalida, digite de 0 a 10]")
            nota = notas.append(float(input("Digite a sua nota: ")))
    media = sum(notas) / len(notas)
    if media >= 7:
        maior7.append(media)
    n_aluno += 1
print("\nNúmero de alunos com media 7 ou maior: ", len(maior7))
