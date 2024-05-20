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

# Solução do videio -----------------------------------------------------------------------------------------

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Trasferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
