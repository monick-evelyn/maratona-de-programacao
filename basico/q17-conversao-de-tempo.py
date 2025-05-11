segundos = int(input())
minutos = 0
horas = 0
while segundos >= 60:
    if (segundos >= 60 and segundos < 3600):
        minutos = segundos//60
        segundos -= minutos * 60
    elif (segundos >= 3600):
        horas = segundos//3600
        segundos -= horas * 3600
    else:
        segundos = segundos
print(f"{horas}:{minutos}:{segundos}")