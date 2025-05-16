lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']

lanche[2] = 'Sorvete' #Substitui 'Pizza' (indice 2) por 'Sorvete'
lanche.append('Biscoito') #Adiciona um elemento ao final da lista
lanche.insert(2 ,'Cachorro-quente') #Adicona um elemento ao índice x

del lanche[3] #Remove o elemento no indíce x
lanche.pop(0) #Remove o elemento no indíce x
lanche.pop() #Remove o último elemento
lanche.remove('Suco') #Remove o elemento

#opção para não quebrar:
if 'Suco' in lanche:
    lanche.remove('Suco') 
    #Remove o elemento apenas se estiver na lista

lanche.sort() #ordena em ordem A-Z/crescente
lanche.sort(reverse=True) #ordena em ordem decrescentre/Z-A 

#cria uma lista ordenada entre 4 e 11, pulando de 1 em 1. 
#(estrutura start, stop, step)
valores = list(range(4, 11, 1))

tamanho = len(valores) # retorna o tamanho da lista

for v in valores:
    print(f"{v} ", end="") #4 5 6 7 8 9 10

for c, v in enumerate(valores):
    print(f"Posição {c}: {v}") #Posição 1: 5...(c começa de 1)

a = [2, 3, 4, 4]
b = a #cria uma ligação entre lista
b[2] = 8 #altera nas suas
print(f'Lista A: {a}') #Lista A: [2, 3, 8, 4]
print(f'Lista B: {b}') #Lista B: [2, 3, 8, 4]

a = [2, 3, 4, 4]
b = a [:] #cria uma cópia
b[2] = 8
print(f'Lista A: {a}') #Lista A: [2, 3, 4, 4]
print(f'Lista B: {b}') #Lista B: [2, 3, 8, 4]