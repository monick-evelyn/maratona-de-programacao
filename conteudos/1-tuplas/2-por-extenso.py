por_extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco'

num = int(input("Digite um número de 0 a 5: "))
while num > 5 or num < 0:
    num = int(input("Tente novamente. Digite um número de 0 a 5: "))

print(f"Você digitou o número {por_extenso[num]}")