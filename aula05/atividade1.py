listanomes = ["ale", "joao", "max", "bob"]

for i in range(len(listanomes)):
    for j in range(i + 1, len(listanomes)):
     print(listanomes[j], listanomes[i])