# Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionario. No final mostre o conteúdo da estrutura na tela


aluno = dict()

aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif aluno['media'] < 7 and aluno['media'] >= 6.5:
    aluno['situacao'] = 'RECUPERAÇÃO'
else:
    aluno['situacao'] = 'REPROVADO'

print(f'Nome     é igual a {aluno["nome"]}')
print(f'Média    é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["situacao"]}')

# SOLUÇÃO DO VIDEO ----------------------------------------------------------------------
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situcao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')

''' OBS
med = 5.1
( 5 <= med < 7 )  <-- this expression is the same as this --> ( med < 7 and med >= 5 )
>>> med = 5
>>> 5 <= med < 7
True
>>> med < 7 and med >= 5
True
>>> med = 5.1
>>> 5 <= med < 7
True
>>> med < 7 and med >= 5
True
>>> med = 7.5
>>> 5 <= med < 7
False
>>> med < 7 and med >= 5
False

'''
