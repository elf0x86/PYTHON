# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
valores = dict()

for x in range(0, 4):
    valores[f'jogador{x}'] = randint(0, 10)
print(valores)


res = {key: val for key, val in sorted(valores.items(), key = lambda ele: ele[1], reverse = True)}


print('Valores sorteados:')
for key, value in valores.items():
    print(f'    O {key} tirou {value}')


print('Ranking so jogadores:')
for key, value in res.items():
    print(f'    O {key} tirou {value}')

# SOLUÇÃO DO VIDEO -------------------------------------------------------------------
from random   import randint
from time     import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados...')
for k, v in jogo.items():
    print(f'   {k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # retorna um tupla
print('-=' * 30)
print(' == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)

# SOLUÇÃO DOS COMENTARIOS ------------------------------------------------------------
from random import randint
from time import sleep

lugar=0
jo={}

print('=====Valores Sorteados:')

for i in range(1, 5):
        jo[f'Jogador{i}'] = randint(1, 6)
        print(f'  Jogador {i} jogou o dado e obteve o valor: {jo[f"Jogador{i}"]}')
        sleep(0.5)
print('='*40)

for i in range(1, 5):
    if jo['Jogador1'] >= jo['Jogador2'] and  jo['Jogador1'] >=  jo['Jogador3'] and jo['Jogador1'] >= jo['Jogador4'] and jo['Jogador1'] != 0:
        lugar+=1
        print(f'Jogador1 ficou em {lugar}° lugar com {jo["Jogador1"]} no dado. {jo}')
        jo['Jogador1']=0

    if jo['Jogador2'] >= jo['Jogador1'] and  jo['Jogador2'] >=  jo['Jogador3'] and jo['Jogador2'] >= jo['Jogador4'] and jo['Jogador2'] != 0:
        lugar+=1
        print(f'Jogador2 ficou em {lugar}° lugar com {jo["Jogador2"]} no dado. {jo}')
        jo['Jogador2']=0

    if jo['Jogador3'] >= jo['Jogador1'] and  jo['Jogador3'] >=  jo['Jogador2'] and jo['Jogador3'] >= jo['Jogador4'] and jo['Jogador3'] != 0:
        lugar+=1
        print(f'Jogador3 ficou em {lugar}° lugar com {jo["Jogador3"]} no dado. {jo}')
        jo['Jogador3']=0
    if jo['Jogador4'] >= jo['Jogador1'] and  jo['Jogador4'] >=  jo['Jogador3'] and jo['Jogador4'] >= jo['Jogador2'] and jo['Jogador4'] != 0:
        lugar+=1
        print(f'Jogador4 ficou em {lugar}° lugar com {jo["Jogador4"]} no dado. {jo}')
        jo['Jogador4']=0

print(jo)

