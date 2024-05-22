# crie uma matriz de dimensão 3x3 e preencha com valore lidos pelo teclado
# no final, mostre a matriz na tela, com a formatação correta.

matrix = list()
tmp = list()

for x in range(0, 3):
    for y in range(0, 3):
        tmp.append(input(f'Digite um valor para [{x}, {y}]: '))
    matrix.append(tmp[:])
    tmp.clear()

for x in range(0, 3):
    for y in range(0, 3):
        print(f'[ {matrix[x][y]} ]', end='')
    print()

