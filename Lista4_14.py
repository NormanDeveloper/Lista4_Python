sim = 0
perhuntas = ["Telefonou para a vitima? [s/n]: ",
             "Esteve no local do crime? [s/n]: ",
             "Mora perto da vitima? [s/n]: ",
             "Devia para a vitima? [s/n]: ",
             "Já trabalhou com a vítima? [s/n]: "
             ]
for i in range(len(perhuntas)):
    resposta = input(perhuntas[i])
    if resposta == 's':
        sim += 1
if sim == 2:
    print("\nSuspeita!")
elif sim > 2 and sim <= 4:
    print("\nCumplice!")
elif sim == 5:
    print("\nAssassino!")
else:
    print("\nInocente!")