# Crie um programa que vai ler vário números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores impares digitados, respectivamente. Ao final mostre
# o conteúdo das três listas geradas

lista = list()
lista_par = list()
lista_impar = list()
resp  = ' '

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)

    if valor % 2 == 0:
        lista_par.append(valor)
    elif valor % 2 == 1:
        lista_impar.append(valor)

    resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break

print('=-' * 30)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {lista_par}')
print(f'A lista de impares é: {lista_impar}')
