# Aprovar o empéstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar. A prestação mensal, não pode exceder 30% do slário ou então o empréstimo 
# será negado


casa = float(input('Valor da casa R$: '))
salario = float(input('Salário do comprador R$: '))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12)
print(f'Para pagar uma casa de R${casa:.2f} em {anos:.2f} anos.')
print(f'A prestacao será de R${prestacao:.2f}')

percentual_salario = (salario * 30 / 100)
if prestacao <= percentual_salario:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
