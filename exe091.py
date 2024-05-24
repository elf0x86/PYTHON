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


