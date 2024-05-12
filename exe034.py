# Escreva um programa que pergunte o slário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.


salario = float(input('Qual é o seu salario R$: '))

if salario > 1250:
    novo_salario = salario + (salario * 10 / 100)
    print(f'Com um salário de R${salario} voce recebe um aumento de  10%. passando a receber R${novo_salario}')
elif salario <= 1250:
    novo_salario = salario + (salario * 15 / 100)
    print(f'Com um salário de R${salario} voce recebe um aumento de  15%. passando a receber R${novo_salario}')
else:
    print('salario invalido')
