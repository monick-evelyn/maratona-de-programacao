#dados = dict()
dados = {'nome':'Pedro', 'idade': 25}
print(dados['nome']) #Pedro
print(dados['idade']) #25

dados['sexo'] = 'M' #adiciona chave e elemento
print(dados) #{'nome': 'Pedro', 'idade': 25, 'sexo': 'M'}

del(dados['idade']) #remove a idade
print(dados) #{'nome': 'Pedro', 'sexo': 'M'}

#========================================================

filme = {'titulo': 'StarWars',
         'ano': 1977,
         'diretor': 'George Lucas'
         }
print(filme.values()) #Apenas os valores
print(filme.keys()) #Apenas as chaves
print(filme.items()) #Chaves e valores

for chave, valor in filme.items():
    print(f'{chave}: {valor}')
    #titulo: StarWars
    #ano: 1977
    #diretor: George Lucas

locadora = list()
locadora.append(filme)
print(locadora) 
#[{'titulo': 'StarWars', 'ano': 1977, 'diretor': 'George Lucas'}]