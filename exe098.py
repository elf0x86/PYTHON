# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# inicio, meio, fim e realize a contagem. Seu programa tem que realizar três contagens através
# da funão criada: 
# A) de 1 até 10 de 1 em 1
# B) de 10 até o de 2 em 2
# C) Uma contagem personalizada
from time import sleep


def msg(simbolo='=', repeticao=20):
    print(f'{simbolo}' * repeticao)


def exemplo():
    msg()
    for x in range(1, 11):
        print(x, end=' ')
        if x == 10:
            print('FIM!')

    msg('-')
    for x in range(10, 0, -1):
        print(x, end=' ')
        if x == 1:
            print('FIM!')
    msg()


def contador(inicio=0, fim=0, passo=1):
    msg('=')
    if inicio == fim:
        print('Range invalido 0 até zero')

    if inicio < fim:
        print('inicio < fim')
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for x in range(inicio, fim+1, passo):
            print(f'{x} ', end='')
    if inicio < fim and passo < 0:
        passo = int(str(passo)[1:])
        print('inicio < fim')
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for x in range(inicio, fim+1, passo):
            print(f'{x} ', end='')


    if inicio > fim:
        print('inicio > fim')
        print(f'Contagem de {fim} até {inicio} de {passo} em {passo}')
        for x in range(inicio, fim, -passo):
            print(f'{x} ', end='')
    if inicio > fim and passo < 0:
        print('inicio > fim or passo < 0')
        passo = int(str(passo)[1:])
        print(f'Contagem de {fim} até {inicio} de {passo} em {passo}')
        for x in range(inicio, fim, -passo):
            print(f'{x} ', end='')

    print('FIM!')

# PROGRAMA PRINCIPAL

exemplo()
print(f'\nAgora é sua vez de personalizar a contagem!')
inicio = int(input(f'{"INICIO:": <10}'))
fim    = int(input(f'{"FIM:": <10}'))
passo  = int(input(f'{"PASSO:": <10}'))

if passo == 0:
    passo = 1

contador(inicio, fim, passo)

