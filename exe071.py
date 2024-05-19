# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar cada valor que serão entregues.
# OBS: considerando que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


count_50 = 0
count_20 = 0
count_10 = 0
count_1  = 0

valor_saque = float(input('Quanto você deseja sacar R$: '))
valor_saque = int(valor_saque)
bkp_valor_saque = valor_saque

while valor_saque != 0:

    print(valor_saque)

    if (valor_saque - 50) >= 50 or (valor_saque - 50) == 0:
        valor_saque -= 50
        count_50 += 1
    elif (valor_saque - 20) >= 20 or (valor_saque - 20) == 0:
        valor_saque -= 20
        count_20 += 1
    elif (valor_saque - 10) >= 10 or (valor_saque - 10) == 0:
        valor_saque -= 10
        count_10 += 1
    elif (valor_saque - 1) >= 1 or (valor_saque - 1) == 0:
        valor_saque -= 1
        count_1 += 1

print(f'Você recebera {count_50} notas de R$50')
print(f'Você recebera {count_20} notas de R$20')
print(f'Você recebera {count_10} notas de R$10')
print(f'Você recebera {count_1} notas de R$1')



# Solução do video ------------------------------------------------------------------
print('=' * 30)
print(f'{"BANCO CEV":^30}')
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$: '))
total = valor
ced   = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')


