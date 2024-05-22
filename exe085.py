# Crie um programa onde o usuário possa digitar sete valores numéricos e coadastre-os em uma
# lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores
# pares e ímpares em ordem crescente.

valores = [[], []]
pares   = list()
impares = list()

for x in range(0, 7):
    valor = int(input(f'Digite o {x+1}º valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

pares   = valores[0][:]
impares = valores[1][:]

print(f'Lista de valores: {valores}')

pares.sort()
print(f'Lista de valores pares {pares}')

impares.sort(reverse=True)
print(f'Lista de valores impares {impares}')
