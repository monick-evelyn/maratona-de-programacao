brasil = list()
estado = {}
chave = ''
contador = 0

while chave != 'N':
    estado['uf'] = input("Digite o UF: ")
    estado['sigla'] = input("Digite a sigla: ")
    contador +=1
    #brasil.append((estado)) faz uma ligação
    brasil.append(estado.copy()) #faz uma cópia
    chave = input(f"Deseja continuar ({contador} estado(s) até agora)? ").upper()

for e in brasil:
    print(e)
    for chave, valor in e.items():
        print(f'{chave}: {valor}' )