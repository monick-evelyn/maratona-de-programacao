pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0]) #Pedro
print(pessoas[2][0]) #João
print(pessoas[1]) #['Maria', 19]

teste = list()
teste.append('Gustavo')
teste.append(40)
print (teste) #['Gustavo', 40]

galera = list()
#galera.append(teste) - ligação entre listas
galera.append(teste[:]) #cópia
galera.append(['Paula', 18])
print(galera) #[['Gustavo', 40], ['Paula', 18]]

for p in galera:
    print(f"{p[0]} tem {p[1]} anos")
    #Gustavo tem 40 anos
    #Paula tem 18 anos