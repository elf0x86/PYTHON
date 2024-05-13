# Calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque : 10% de desconto
# - à vista no cartão       : 5%  de desconto
# - em até 2x no cartão     : preço normal
# - 3x ou mais no cartão    : 20% de juros


nome='AMAZON'
print(f'============ LOJAS {nome} ============') 
compras = int(input('Preço das compras R$: '))

opcao   = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Opção: '''))

if opcao == 1:
    valor = compras - (compras * 10 / 100)
    print(f'Sua compra à vista vai custar R${valor}')
elif opcao == 2:
    valor = compras - (compras * 5 / 100)
    print(f'Sua compra à vista no cartão vai custar R${valor}')
elif opcao == 3:
    valor = compras
    print(f'Sua compra 2x no cartão vai custar R${valor / 2} um total de R${valor}')
elif opcao == 4:
    valor = compras + (compras * 20 / 100)
    print(f'Sua compra em 3x ou mais no cartão vai custar R${valor / 3} um total de R${valor}')
else:
    print(f'Opção invalida de pagamendo. Tente novamente')
