# Faça um programa que thenha uma função chamada maior(), que receba vários parâmetros com
# valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior

from time import sleep
from random import randint

def maior(* num):
    print('=' * 40)
#    print(f'O tipo eh: {type(num)}')
    print(f'Analisando os valores passados...')
    for v in range(0, len(num)):
        print(num[v], end=' ', flush=True)
        sleep(0.3)

    for i,n in enumerate(num):
        if i == 0:
            maior = n
        if n > maior:
            maior = n
    print(f'O maior número entre {num} é {maior}')
  

def gera_numeros(i=0, f=10):
    myList = list()
    while i != f:
        if i == 0:
            primeiro_valor = randint(0, 99)
        
        segundo_valor  = randint(0, 99)  
        if myList.count(segundo_valor) not in myList:
            myList.append(segundo_valor)
            i += 1

    return myList


maior(1,2,3,5,7)
maior(3,6,9,3,11,3,9)

''' Testes
maior(gera_numeros())

numeros_gerados = list()
for x in range(0, 10):
    numeros_gerados.append(gera_numeros())

for x in range(0, len(numeros_gerados)):
    print('=+' * 40)
    print(f'Os numeros gerados foram {numeros_gerados[x]}')
    for y in range(0, len(numeros_gerados[x])):
        maior(numeros_gerados[y])
'''

# SOLUÇÃO DO VIDEO ------------------------------------------------------------------------------------
def maior2(*num):
    cont = maior = 0
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

# Programa Principal --------------------------------------------------
maior(3,5,6,8,5,3,2)
maior(3,5,6)
maior(1, 2)
maior(3)
maior() # Ta dando erro
