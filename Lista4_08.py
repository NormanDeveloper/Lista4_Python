idade = []
altura = []
n_pessoa = 1
for i in range(5):
    print("\nPessoa n°", n_pessoa)
    u_idade = idade.append(int(input("Digite a idade: ")))
    u_altura = altura.append(float(input("Digite a altura: ")))
    n_pessoa += 1
idade.reverse()
altura.reverse()
print("\nIdades: ", idade, "\nAltura: ", altura)
