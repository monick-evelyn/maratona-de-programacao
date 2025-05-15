lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
numeros = 1,2,3,4,4

print(lanche) #('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1]) #Suco
print(lanche[1:]) #('Suco', 'Pizza', 'Pudim')
print(lanche[1:3]) #('Suco', 'Pizza')
print(lanche[:3]) #('Hamburguer', 'Suco', 'Pizza')

for comida in lanche: #percorre todos os elementos da tupla
    print(f"Eu vou comer {comida}")
    #print(f"{comida}", end=" ")

print(f"\n{len(lanche)}") #retorna o tamanho da tupla: 4

print(sorted(lanche)) #Coloca a lista em ordem alfabética (A-Z) ou crescente

print(lanche.count('Hamburguer')) #1: Conta quantas vezes o elementos aparece

print(lanche.index('Pizza')) #2: Conta o index do elemento (primeira ocorrência)
print(numeros.index(4, 4)) #4: Onde está o número 4 a partir da posição 4

c = lanche + numeros #"cola" as tuplas
print(c) #('Hamburguer', 'Suco', 'Pizza', 'Pudim', 1, 2, 3, 4, 4)