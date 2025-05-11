tempo_gasto = int(input())
velocidade_media = int(input())
#12 KM/L
distancia = velocidade_media * tempo_gasto
combustivel_gasto = distancia/12
print(f"{combustivel_gasto:.3f}")