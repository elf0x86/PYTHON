# Ler o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

'''
peso = float(input(f'Peso da 1º pessoa: '))
maior = peso
menor = peso


for x in range(2, 6):
    peso = float(input(f'Peso da {x}º pessoa: '))

    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'O MARIO peso lido foi de {maior}Kg.')
print(f'O MENOR peso lido foi de {menor}Kg.')
'''

# ======= codigo do video ======== 
mario = 0
menor = 0
for x in range(1, 5):
    peso = float(input(f'Peso da {x}º pessoa: '))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O MARIO peso lido foi de {maior}Kg.')
print(f'O MENOR peso lido foi de {menor}Kg.')

