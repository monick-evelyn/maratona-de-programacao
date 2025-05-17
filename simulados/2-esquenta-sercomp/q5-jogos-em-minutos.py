h_inicial, min_inicial, h_final, min_final = input().split(" ")
h_inicial = int(h_inicial)
h_final = int(h_final)
min_inicial = int(min_inicial)
min_final = int(min_final)

horas = h_final - h_inicial
minutos = min_final - min_inicial

max_horas = 24
min_minuto = 1
max_minuto = 60

if (minutos < 0):
    horas = horas + minutos
    minutos = (minutos * -1) * max_minuto + minutos

if (minutos > max_minuto):
    aux = minutos
    minutos = minutos - ((minutos//max_minuto) * max_minuto)
    horas = horas + aux//max_minuto

if (horas == 0 and minutos == 0):
    horas = max_horas

if (horas < 0):
    horas = max_horas + horas
print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")