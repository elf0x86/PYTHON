# Leia nome e peso de várias pessoas, guradando tudo em uma lista. No final mostre
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoa  = list()
pessoas = list()
resp = ' '
while True:
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa[:])
    pessoa.clear()

    resp = input('Quer Continuar? [S/N]: ').strip().upper()[0]
    while resp not in 'NS':
        resp = input('Quer Continuar? [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break

print('-=' * 40)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

maior_peso = 0
menor_peso = 0
for p in enumerate(pessoas):
    if maior_peso == 0:
            maior_peso = p[1][1]
    elif p[1][1] >= maior_peso:
            maior_peso = p[1][1]

    if menor_peso == 0:
        menor_peso = p[1][1]
    elif p[1][1] <= menor_peso:
        menor_peso = p[1][1]


nomes_pessoas_maior_peso = list()
nomes_pessoas_menor_peso = list()
for x in enumerate(pessoas):
    if x[1].count(maior_peso) == 1:
        nomes_pessoas_maior_peso.append(x[1][0])
    if x[1].count(menor_peso) == 1:
        nomes_pessoas_menor_peso.append(x[1][0])

print(f'O maior peso foi de {maior_peso}Kg. Nome(s) {nomes_pessoas_maior_peso}')
print(f'O menor peso foi de {menor_peso}Kg. Nome(s) {nomes_pessoas_menor_peso}')

""" TESTE FEITO NO INTERPRETADOR

>>> pessoas = [['Maria', 70.0], ['joao', 100.0], ['cladio', 85.0], ['Helio', 100.0], ['ana', 70.0], ['gustavo', 88.0]]
>>> pessoas[0].index(100)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 100 is not in list
>>> maior = 100
>>> pessoas.index(100)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 100 is not in list
>>> pessoas.count(100)
0
>>> pessoas.count(100.0)
0
>>> for x in pessoas:
... print(x)
  File "<stdin>", line 2
    print(x)
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>>



>>> for x in pessoas:
...     print(x)
...
['Maria', 70.0]
['joao', 100.0]
['cladio', 85.0]
['Helio', 100.0]
['ana', 70.0]
['gustavo', 88.0]
>>> for x in pessoas:
...     print(x[1].count(100))
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
AttributeError: 'float' object has no attribute 'count'
>>> for x in pessoas:
...     print(x.count(100))
...
0
1
0
1
0
0
>>> for x in enumerate(pessoas):
...     print(x)
...
(0, ['Maria', 70.0])
(1, ['joao', 100.0])
(2, ['cladio', 85.0])
(3, ['Helio', 100.0])
(4, ['ana', 70.0])
(5, ['gustavo', 88.0])
>>> for x in enumerate(pessoas):
...     print(x[0], x[1].count(100))
...
0 0
1 1
2 0
3 1
4 0
5 0
>>> for x in enumerate(pessoas):
...     if x[1].count(100) == 1:
...             print(x[1][0])
...
joao
Helio
>>> for x in enumerate(pessoas):
...     if x[1].count(maior) == 1:
...             print(f'nome: {x[1][0]\npeso: {x[1][1]}')
  File "<stdin>", line 3
    print(f'nome: {x[1][0]\npeso: {x[1][1]}')
                                            ^
SyntaxError: f-string expression part cannot include a backslash
>>> for x in enumerate(pessoas):
...     if x[1].count(maior) == 1:
...             print(f'nome: {x[1][0]}\npeso: {x[1][1]}')
...
nome: joao
peso: 100.0
nome: Helio
peso: 100.0
>>> pessoas
[['Maria', 70.0], ['joao', 100.0], ['cladio', 85.0], ['Helio', 100.0], ['ana', 70.0], ['gustavo', 88.0]]
>>> maior = 0
>>> for p in enumerate(pessoas):
...     if maior == 0:
...             maior = p[1][1]
...     elif p[1][1] >= maior:
...             maior = p[1][1]
...
>>> maior
100.0
>>>
"""
# SOLUÇÃO DO VIDEO ---------------------------------------------------------------------
temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas. ')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()

