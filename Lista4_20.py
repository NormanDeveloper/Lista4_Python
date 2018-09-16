salarios = []
abonos = []
salario = True
n_funcionario = 1
while salario != 0:
    print("\nFuncionario n°", n_funcionario)
    salario = float(input("Digite o salario: "))
    if salario == 0:
        break
    else:
        while salario < 0:
            print("[salario inválido]")
            print("\nFuncionario n°", n_funcionario)     
            salario = float(input("Digite o salario novamente: "))
        abono = abonos.append(salario * 0.2)
        salarios.append(salario)
    n_funcionario += 1
print("\n" * 3)
valor_minimo = 0
for i in range(len(salarios)):
    if abonos[i] <= 100:
        print("Salario = R$", salarios[i], " - Abono = R$ 100.0")
        abonos[i] = 100
        valor_minimo += 1
        continue
    print("Salario = R$", salarios[i], " - Abono = R$", abonos[i])
print("\nForam precessados", len(salarios), "colaboradores.")
print("Total gasto com abonos: R$", sum(abonos))
print("Valor minimo pago a ", valor_minimo, "colaboradores.")
print("Maior valor de abono pago: ", max(abonos))