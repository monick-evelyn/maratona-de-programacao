#diamante = "<>"

#<..><.<..>>
#<<<..<......<<<<....>
casos = int(input())
for i in range(casos):
    linha = input()
    #pilha para armazenar '<'
    pilha = []

    diamantes = 0
    # Se o caractere for '>' e houver um '<' na pilha,
    # significa que um diamante foi formado
    for caractere in linha:
        if caractere == '<':
            pilha.append('<')
        elif caractere == '>' and pilha:
            pilha.pop()
            diamantes += 1
    
    print(diamantes)