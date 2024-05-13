# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a didade:
# Até 9 anos  : MIRIM       Até 19 anos : JUNIOR
# Até 14 anos : INFANTIL    Até 25 anos : SÊNIOR

from datetime import date

ano_atual = date.today().year
ano_nascimenot = int(input('Ano de Nascimento: '))

idade = ano_atual - ano_nascimenot
print(f'O atleta tem {idade} anos.')


if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JUNIOR')
elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR')

