h_inicial, min_inicial, h_final, min_final = map(int, input().split())

# Converte hora e minuto de início/fim para minutos totais
inicio = h_inicial * 60 + min_inicial
fim = h_final * 60 + min_final

# Se o tempo final for menor ou igual ao inicial, 
# o jogo passou da meia-noite
if fim <= inicio:
    fim += 24 * 60  # adiciona 24 horas em minutos

# Duração total em minutos
duracao_total = fim - inicio

# Converte para horas e minutos
horas = duracao_total // 60
minutos = duracao_total % 60

# Exibe o resultado
print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
'''
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
'''