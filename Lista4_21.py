veiculos = ['Fusca', 'Palio', 'UNO', 'Ferrari', 'HB20']
consumo_carros = []
for i in range(5):
    print("Veiculo n°", i + 1, "\nNome: ", veiculos[i])
    km_litro = float(input("Km por litro: "))
    consumo_carros.append(km_litro)

print("\nRelatório final: ")
for i in range(5):
    print(i+1, " - ", veiculos[i], " - ", consumo_carros[i], " - ", round(1000 / consumo_carros[i], 2), " - R$", round(1000 / consumo_carros[i] * 2.25, 2))
indice_menor_consumo = consumo_carros.index(max(consumo_carros))
print("O menor consumo é o do ", veiculos[indice_menor_consumo])