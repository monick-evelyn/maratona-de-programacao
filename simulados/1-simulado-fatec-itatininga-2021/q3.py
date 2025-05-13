n = int(input())
sequencia = 0
lista = []
for i in range(1, (n * 4) + 1):
    lista.append(i)
    if (lista[i - 1] % 4 != 0):
        print(lista[i - 1], end=",")
    if (i % 4 == 0):
        lista[i - 1] = "PIM"
        print(lista[i -1])