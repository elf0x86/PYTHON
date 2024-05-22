# Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso, mostre:
# A) Quantos números foram digitados
# B) A lista de valores ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista

lista = list()
resp  = ' ' 

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)

    resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break

print(f'Voce digitou {len(lista)} elementos em {lista}')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if lista.count(5) >= 1:
    print(f'O valor 5 foi encontrado na lista!')
else:
    print(f'O valor 5 não foi encontrado na lista!')
