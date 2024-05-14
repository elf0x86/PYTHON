# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input('Digite um número: '))
primo_div_count = 0
composto_div_count = 0
msg = ''
controle = 0

for x in range(1, num+1):
    if num % x == 0:
        print(f'\033[1;33m{x}\033[m', end=' ')
        primo_div_count += 1
        composto_div_count += 1
    else:
        print(f'\033[1;31m{x}\033[m', end=' ')

    if primo_div_count == 2:
        msg=f'O número {num} foi divisível {primo_div_count} vezes\nE por isso ele É PRIMO!'
    else:
        msg=f'O número {num} foi divisível {composto_div_count} vezes\nE por isso ele NÃO É PRIMO!'

    if controle == 10:
        print()
        controle = 0
    else:
        controle += 1

print('\n',msg)


# Solução do video -------------------------

num = int(input('Digite um número: '))
tot = 0

for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[1;33m{c}', end=' ')
        tot += 1
    else:
        print(f'\033[3;31m{c}', end=' ')

print(f'\n\033[mO número {num} foi divisível \033[1;33m{tot} vezes.\033[m')
if tot == 2:
    print(f'Por isso ele é PRIMO')
else:
    print(f'Por isso ele é COMPOSTO')



