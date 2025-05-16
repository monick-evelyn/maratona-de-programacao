matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #estrutura
#for de alimentação
for linha in range(3): #[0,0,0]
    for coluna in range (3): #0
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: ")) 
#for de print
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end="")
    print()