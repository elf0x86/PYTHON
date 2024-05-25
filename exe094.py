# Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario
# e todos os dicionários em uma lista. No final mostre:
# A) quantas pessoas foram cadastradas 
# B) A média de idade do grupo
# C) uma lista com todas as mulheres
# D) Uma lista com todas as pessoas com idade acima da média


pessoa  = dict()
PESSOAS = list()
mulheres_cadastradas = list()
tot_pe = 0
media  = 0

while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo [M/F]: ')

    if pessoa['sexo'] == 'F':
        mulheres_cadastradas.append(pessoa['nome'])

    while pessoa['sexo'] not in 'MF':
        print('\033[1;33mOPÇÃO INVALIDA\033[m')
        pessoa['sexo'] = input('Sexo [M/F]: ')

    pessoa['idade'] = int(input('Idade: '))

    PESSOAS.append(pessoa.copy())
    pessoa.clear()

    resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break

tot_p = len(PESSOAS)
for x in range(0, tot_p):
    media = media + PESSOAS[x]['idade']

media = media / tot_p

print(f'- O grupo tem {tot_p} pessoas.')
print(f'- A média de idade é {media:.1f} anos.')
print(f'- As mulheres cadastradas foram: {mulheres_cadastradas}.')
print(f'- Lista das pessoas que estão acima da média\n')

for i in range(0, tot_p):
    if PESSOAS[i]['idade'] > media:
        print(f'--> nome = {PESSOAS[i]["nome"]}; sexo {PESSOAS[i]["sexo"]}; idade {PESSOAS[i]["idade"]};')

# SOLUçÃO DO VIDEO ------------------------------------------------------------
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa ['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('--'* 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print (f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print (f'{p["nome"]}', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
                           
