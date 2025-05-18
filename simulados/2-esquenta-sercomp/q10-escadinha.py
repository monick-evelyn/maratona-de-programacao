import sys
tamanho = int(input())
#lê toda a linha como string e separa os elementos por espaço:
#independe da quant. de espaços entre números
sequencia = sys.stdin.readline().split()

for i in range(tamanho):
    sequencia[i] = int(sequencia[i]) #convete para int

escadinha = 1
if(tamanho == 1 or tamanho == 2):
    print(escadinha)
else:
    dif_atual = sequencia[0] - sequencia[1]
    for i in range(1, tamanho - 1):
        dif_nova = sequencia[i] - sequencia[i+1]
        if (dif_nova != dif_atual):
            dif_atual = dif_nova
            escadinha += 1
    print(escadinha)

#LÓGICA:
#[0][1][2][3][4][5][6][7] (índices)
# 1  1  1  3  5  4  8  12 (números)
#dif_atual = 0 (sequencia[0] - sequencia[1])
#dif_nova = 0 (sequencia[1] - sequencia[2])