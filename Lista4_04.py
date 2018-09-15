caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
vogais = ['a', 'e', 'i', 'o', 'u']
count = 0
while count < 5:
    if vogais[count] in caracteres:
        caracteres.remove(vogais[count])
    count += 1
print("\nExistem", len(caracteres), "consoantes")
print("Elas são : ", caracteres)
