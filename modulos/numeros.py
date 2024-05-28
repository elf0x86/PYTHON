'''
import uteis
# Importa todas as funções de um arquivo chamado uteis.py (se ele existir)

num = int(input('Numero: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {uteis.dobro(num)}.')


from uteis import fatorial, dobro
# Essa forma de importar não é recomendada pelo python. 
# Pode haver incompatibilidades com os nomes

num = int(input('Numero: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {dobro(num)}.')
'''



from uteis import numeros
# uteis é agora um pacote que contem uma pasta:
# numeros/__init__.py que são as funções para lidar com numeros

num = int(input('Numero: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {numeros.dobro(num)}.')


