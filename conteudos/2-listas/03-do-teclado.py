chave = ""
valores = []
while chave != "N":
    num = int(input("Digite um valor: "))
    if (num in valores):
        print("Valor duplicado! Não vou adicionar...")
    else:
        valores.append(num)
    chave = input("Quer continuar (S/N)? ").upper()

valores.sort()
print(f"Você digitou os valor {valores}")