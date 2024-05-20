# Crie um programa que tenha uma tupla única com nomes de produtos e seus
# respectivos preços, na sequência. No final, mostre um listagem de preços
# organizando os dados em forma tabular

#produtos = (input('Nome: '), int(input('Valor: ')),input('Nome: '), int(input('Valor: ')),input('Nome: '), int(input('Valor: ')),input('Nome: '), int(input('Valor: ')))

produtos = ('Notebook', 1250, 'Phone', 1045, 'Printer', 571, 'Mouse', 320)
cont = 0
print('-' * 40)
for x in range(0, len(produtos)):
    if cont == 0:
        print(f'Produto: {produtos[x]: <10}', end='')
        cont = 1
    elif cont == 1:
        print(f'Preço: R${produtos[x]}')
        cont = 0
print('-' * 40)
print(produtos)
