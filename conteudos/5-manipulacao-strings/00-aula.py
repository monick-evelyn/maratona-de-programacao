frase = 'Curso em Vídeo Python' #tupla de strings

#Fatiamento
#(caractere no índice 9)
print(frase[9])#V 
#(caractere do 9 ao 12 indice)
print(frase[9:13]) #Víde 
#(caractere do 9 ao 20 pulando de 2 em 2)
print(frase[9:21:2]) #VdoPto 
#(do 0 ao 4)
print(frase[:5]) #Curso 
#(do 15 até o fim)
print(frase[15:]) #Python
#(do 9 até o final pulando de 3 em 3)
print(frase[9::3]) #VePh 

#Análise
#quant de caracteres
tamanho = len(frase) #21
#Conta quantos "o" tem na string toda
print(frase.count("o")) #3
#Conta quantos "o" tem na string de 0 ao 12 caractere
print(frase.count("o", 0, 13)) #1
#Indica onde começa "deo"
print(frase.find("deo")) #11 (se não encontrar, retorna -1)

print('Curso' in frase) #True

#Transformação
#Substitui as palavras 'Python' por 'Android'
print(frase.replace('Python', 'Android')) #Curso em Vídeo Android
#maiúsculas
print(frase.upper()) #CURSO EM VÍDEO PYTHON
#minúsculas
print(frase.lower()) #curso em vídeo python
#só o primeiro em maiúsculo
print(frase.capitalize()) #Curso em vídeo python
#A primeira letra de cada palavra maiúsculo
print(frase.title()) #Curso Em Vídeo Python

frase2 = "   Aprenda Python  "
#Remove espaços do começo e do final
print(frase2.strip()) #'Aprenda Python'
#Remove espaços do final
print(frase2.rstrip()) #'   Aprenda Python'
#Remove espaços do começo
print(frase2.lstrip()) #'Aprenda Python  '

#DIVISÃO
print(frase.split()) #['Curso', 'em', 'Vídeo', 'Python']
print(frase.split()[0]) #Curso

#JUNÇÃO
#junta todos os caracteres por '-'
print('-'.join(frase)) #C-u-r-s-o- -e-m- -V-í-d-e-o- -P-y-t-h-o-n

#OUTRAS
#Textos longos
print("""
      AAAAA AAAAAA AAAAAA AAAAAA AAAAAA 
      AAAA AAAAA AAAA AAAA AAAA AAAAA 
      AAAA AAAA AAAAA AAAAA AAAAA AAAAA 
      AAAAA AAAAAA AAAA AAAAA AAAA AAAA 
      AAAAA AAAAA AAAAA AAAAA AAAAA AAAAAA""")