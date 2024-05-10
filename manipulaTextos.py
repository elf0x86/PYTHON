# Fatiando string

frase = "curso em video python"

print(frase[0:4])       # curs
print(print(frase[0:5]) # curso

print(frase[15:20])  # pytho
print(frase[15:21])  # python
print(frase[15:])    # python

print(frase[9:21:2]) # vdopto
print(frase[9::3])   # vep


# Analisando string
print(len(frase)) # retorna a quantidade de caracteres -> 21
print(frase.count('o')) # quantas vezes aparece a letra 'o' minuscula. -> 3
print(frase.count('o', 0, 13)) # contagem com fatiamento 0:13 quantos 'o' tem -> 1
print(frase.find('deo')) # mostra em que indice começa 'deo' -> 11
print(frase.find('Android')) # mostra -1 significa que não existe dentro de frase
print('curso' in frase) # retorna True se achar a string 'Curso'

# modificando strings com methods 
# obs: "não modifica a variavel só a saída"
# para manter a modificação fazer um reaatribuição ex: frase = frase.upper()

frase.replace('python', 'android') # 'curso em video android'
frase.upper()                      # 'CURSO EM VIDEO PYTHON'
frase.lower()                      # 'curso em video android'
frase.captilize()                  # 'Curso em video python'
frase.tile()                       # 'Curso Em Video Python'

frase = '   Aprenda Python  '
frase.strip()                      # 'Aprenda Python'
frase.rstrip()                     # '   Aprenda Python'
frase.lstrip()                     # 'Aprenda Python '

# Divisão de strings
frase = 'Curso em Video Python'
frase.split()                      # divide uma string em uma lista onde cada elemento é separado
                                   # por um delimitador. O delimitador padrão é o ' '
                                   # resultado: ['Curso', 'em', 'Video', 'Python']

'--'.join(frase)                   # 'C--u--r--s--o-- --e--m-- --V--i--d--e--o-- --P--y--t--h--o--n'
'--'.join(frase.split())           # 'Curso--em--Video--Python'

frase.split()[1][1]
