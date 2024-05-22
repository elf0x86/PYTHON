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
                                            
