n = float(input())
n = str(n)
partes_n = n.split(".")
inteira = int(partes_n[0])*100
decimal = int(partes_n[1])

moedas = [100, 50, 25, 10, 5, 1]
notas = [10000, 5000, 2000, 1000, 500, 200]

print("NOTAS:")
for nota in notas:
    quantidade = inteira // nota
    inteira = inteira - nota * quantidade
    print(f"{quantidade} nota(s) de R$ {nota/100:.2f}")

print("MOEDAS:")
for moeda in moedas:
    #print(f"Moeda: {moeda}\nDecimal: {decimal}\nInteira: {inteira}")
    if (inteira == moeda):
        quantidade = inteira // moeda
        inteira -= moeda * quantidade
        print(f"{quantidade} moeda(s) de R$ {moeda/100:.2f}")
    else:
        quantidade = decimal // moeda
        decimal -= moeda * quantidade
        print(f"{quantidade} moeda(s) de R$ {moeda/100:.2f}")