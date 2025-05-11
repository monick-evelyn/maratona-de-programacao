n = int(input())
print(n)
#quant. minima de notas de 100, 50, 20, 10, 5, 2 e 1
notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    quantidade = n // nota
    print(f"{quantidade} nota(s) de R$ {nota},00")
    n -= nota * quantidade