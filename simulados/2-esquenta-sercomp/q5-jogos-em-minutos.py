h_inicial, min_inicial, h_final, min_final = input().split(" ")
h_inicial = int(h_inicial)
h_final = int(h_final)
min_inicial = int(min_inicial)
min_final = int(min_final)

horas = h_final - h_inicial
minutos = min_final - min_inicial

max_horas = 24
min_min = 1
max_min = 60

if (minutos < 0):
    horas = horas + minutos
    minutos = (minutos * -1) * max_min + minutos

if (minutos > max_min):
    aux = minutos
    minutos = minutos - ((minutos//max_min) * max_min)
    horas = horas + aux//max_min

if (horas == 0 and minutos == 0):
    horas = max_horas

if (horas < 0):
    horas = max_horas + horas
print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")