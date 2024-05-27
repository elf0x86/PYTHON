# Faça um progrma que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 núemros e vai colocá-los dentro da lista.
# A segunda  função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from random import randint

def sorteia():
    umArr = list()
    num   = 0
    flag  = 0
    while flag != 4:
        if flag == 0:
            umArr.append(randint(0, 10))

        num = randint(0, 10)
        if umArr.count(num) == 0:
            umArr.append(num)
            flag += 1
    return umArr  # SOME TIMES IT RETURNS 6 NUMBERS

def soma_par(umArr):
    tot = 0
    for x in umArr:
        if x % 2 == 0:
            tot += x

    return tot

# PROGRAMA PRINCIPAL
numeros = sorteia()

print(f'Sorteando os {len(numeros)} da lista: ',end='')
for i, v in enumerate(numeros):
    print(f'{v} ', end='')
print('PRONTO!')

print(f'Somando os valores pares de {numeros}, temos {soma_par(numeros)}.', flush=True)
