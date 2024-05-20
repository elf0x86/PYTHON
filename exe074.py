# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
# Depois disso, mostre a listagem de números gerados e também indique o MENOR 
# e o MAIR valor que estão na tupla
from random import randint

aleatorios = (randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10))
menor = maior = 0


print('-' * 40)
for x in range(0, len(aleatorios)):
    if x == 0:
        menor = aleatorios[x]
        maior = aleatorios[x]
    if aleatorios[x] < menor:
        menor = aleatorios[x]
    elif aleatorios[x] > maior:
        maior = aleatorios[x]

    print(f'{x}º Valro da TUPLA: {aleatorios[x]}')

print('-' * 40)
print(f'O maior valor eh: {maior}')
print(f'O menor valor eh: {menor}')
print('-' * 40)
print(aleatorios)

