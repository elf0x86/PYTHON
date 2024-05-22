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

# <shift> + # + k open the manuals of python. Similar to help('if') 
