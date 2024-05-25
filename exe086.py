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

# SOLUÇÃO DO VIDEO
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^6}] ', end='')
    print()
