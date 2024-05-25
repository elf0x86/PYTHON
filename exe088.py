# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo
# em uma lista composta.

from random import randint
jogo = list()
jogos = list()
fim = int(input('Quantos jogos você quer que eu sorteie? '))
msg = f" SORTEANDO {fim} JOGOS "
print(f'{msg:=^40}')

for x in range(0, fim):
    while len(jogo) != 6:
        num = randint(0, 60)

        if len(jogo) == 0:
            jogo.append(num)

        if jogo.count(num) == 0:
            jogo.append(num)
#        else:
#            print(f'Numero {num} já existe dentro da lista {jogo} na posição {jogo.index(num)}')
    jogos.append(jogo[:])
    jogo.clear()

for x in range(0, len(jogos)):
    print(f'Jogo {x+1: >2}: {jogos[x]}')

print(f'{" < BOA SORTE! > ":=^40}')

# <shift> + # + k open the documentation of python. Similar to help('if') 
# SOLUÇÃO DO VIDEO -------------------------------------------------------------------------------
from random import randint
from time   import sleep
lista = list()
jogos = list()
print('-' * 30)
print('    JOGA NA MEGASENA    ')
print('-' * 30)
quant = int(input('Quanto jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '=-' * 3)
for i, l, in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
print('-=' * 5, '< BOA SORTE >', '=-' * 5)

