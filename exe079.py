# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro ele não será adicionado. No final serão exibidos todos os
# valores únicos digitados, em ordem crescente.

resp = ' '
valores = [int(input('Digite um valor: '))]
print('Valor adicionado com sucesso...')
resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

while resp not in 'N':
    tmp = int(input('Digite um valor: '))

    if str(tmp) in str(valores):
        print('Valor Duplicado! Não vou adicionar...')
    else:
        valores.append(tmp)


    resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

#valores = valores.sort(reverse=True)
print('=-' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')
