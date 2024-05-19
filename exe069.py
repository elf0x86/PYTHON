# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quntas mulheres tem menos de 20 anos

idade = 0
sexo  = ' '
flag  = ' '

maior_idade  = 0
total_homens = 0
mulheres     = 0

while True:
    idade = int(input('Idade: '))

    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    
    if idade > 18:
        maior_idade += 1
    if sexo == 'M':
        total_homens += 1
    if idade < 20 and sexo == 'F':
        mulheres += 1
    
    while flag not in 'SN':
        flag = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

    if flag == 'N':
        break
    else:
        flag = ' '
        sexo = ' '

print(f'Total de maiores de 18 anos cadastrados {maior_idade}.')
print(f'Total de homens cadastrados {total_homens}.')
print(f'{mulheres}  mulheres com menos de 20 anos.')

# Solução do video ----------------------------------------------------------------

tot18 = totH = totM20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]')).strip().upper()[0]

    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')

