temperatura_meses = []
meses = ['Janeiro', 'Fevereiro', 'Março','Abril',
    'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
    'Outubro', 'Novembro', 'Dezembro']

for i in range(12):
    print("\nMês de ", meses[i], " :")
    media = temperatura_meses.append(float(input("Digite a temperatura média: ")))

media_anual = sum(temperatura_meses) / 12
print("\n" * 3)
for i in range(12):
    if temperatura_meses[i] > media_anual:
        print("Temperatura a cima da média no mês: ", meses[i])
