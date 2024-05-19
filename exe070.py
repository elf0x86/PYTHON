# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
# se o usuário vai continuar. No final mostre
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.


total_gasto         = 0
custa_mais_mill     = 0
nome_produto_barato = ''

flag = ' '

while True: 
    nome  = str(input('Nome do produto: '))
    preco = float(input('Preço do produgo R$: '))

    if total_gasto == 0:
        menor_preco = preco
    elif preco < menor_preco:
        menor_preco = preco
        nome_produto_barato = nome

    if preco >= 1000:
        custa_mais_mill += 1

    total_gasto += preco

    # Teste condicional para quebrar loop infinito
    while flag not in 'SN':
        flag = str(input("Continuar? [S/N]: ")).strip().upper()[0]

    if flag == 'N':
        break
    else:
        flag = ' '

print(f'Total gasto na compra R$: {total_gasto}')
print(f'{custa_mais_mill} produto(s) que custam mais de R$1000')
print(f'Nomo do produto mais barato é {nome_produto_barato}')

# Solução do video ------------------------------------------------------------------
total = totmil = menor = cont = 0
barato = ''

while True:
    produto = str(input('Nome do Produto: '))
    preco   = float(input('Preço R$: '))
    cont += 1 
    total += preco 
    if preco > 1000:
        totmil += 1

    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{"FIM DO PROGRAMA":-^40}')
print(f'O total da compra foi: {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')


