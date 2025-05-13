qtd = 1
positivos = 0
while qtd <= 6:
    n = int(input(""))
    if (n != 0):
        qtd += 1
        if n > 0:
            positivos += 1
print(positivos)