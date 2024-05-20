# Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista

valores = list()
maior = 0
maior_position = ''

menor = 0
menor_position = ''

for x in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {x}: ')))
    if x == 0:
        maior = valores[x]
        menor = valores[x]
    if valores[x] > maior:
        maior = valores[x]
    if valores[x] < menor:
        menor = valores[x]


print('=-' * 30)
print(f'Você digitou os valores {valores}')
for x in range(0, len(valores)):
#   print(f'{maior} == {valores[x]} --> {maior == valores[x]}')
    if maior == valores[x]:
        maior_position += f'{x}...'
    if menor == valores[x]:
        menor_position += f'{x}...'

print(f'O maior valor digitado foi {maior} nas posições {maior_position}')
print(f'O menor valor digitado foi {menor} nas posições {menor_position}')
~                                                                        
