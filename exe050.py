# Ler seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
'''
Digite um número: 8
Digite um número: 2
Digite um número: 3
Digite um número: 5
Digite um número: 4
Digite um número: 0
Você informou 4 números PARES. E a soma foi de 14
'''

valor = 0
soma  = 0
total_pares = 0


for s in range(0, 6):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        soma += valor
        total_pares+= 1

# print(f'A soma dos numeros PARES é {soma}')
print(f'Você informou {total_pares} números PARES. E a soma foi de {soma}')
