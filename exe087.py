# Aprimore o desafio anterior, mostrando no final:
# A) soma de todos os valores pares digitados.
# B) soma dos valore da terceira coluna
# C) O maior valor da segunda linha

matrix = list()
tmp = list()

pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0

for x in range(0, 3):
    for y in range(0, 3):
        tmp.append(int(input(f'Digite um valor para [{x}, {y}]: ')))
        if tmp[y] % 2 == 0:
            pares += tmp[y]

        if y == 2:
            soma_terceira_coluna += tmp[y]

        if x == 1:
            if y == 0:
                maior_segunda_linha = tmp[y]
            elif tmp[y] > maior_segunda_linha:
                maior_segunda_linha = tmp[y]

    matrix.append(tmp[:])
    tmp.clear()

print(f'=-' * 40)
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[ {matrix[x][y]} ]', end='')
    print()
print(f'=-' * 40)

print(f'A soma dos valores pares é {pares}')
                                            
# SOLUÇÃO DO VIDEO -------------------------------------------------------------------------------
matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = mai = scol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^6}] ', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('=-' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')
