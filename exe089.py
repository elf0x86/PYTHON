# Crie um programa que leia nome e duas notas de vários alunos e gurade
# tudo em uma lista composta. No final, mostre um boletim contendo
# a média de cada um e permita que o usuário possa mostrar as notas de
# cada aluno individualmente


alunos = list()
aluno  = list()
media  = int()
flag   = int()

while True:
    aluno.append(input('Nome: '))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))

    media = (aluno[1] + aluno[2]) / 2

    alunos.append([aluno[0], aluno[1], aluno[2], media])
    
    aluno.clear()

    resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break

print('-' * 40)
print(f'{"NU": <10} {"NOME": <20} {"MEDIA": <20}')
print('-' * 40)
for x in range(0, len(alunos)):
    #print(f'{x: <10} {alunos[x][0]: <20} ')
    print(f'{x: <10} {alunos[x][0]: <20} {alunos[x][3]: <20.2f} ')


print('=' * 40)
while True:
    flag = int(input('Mostrar notas de qual aluno (999 interrope): '))
    if flag == 999:
        break
    else:
        print(f'Notas de {alunos[flag][0]} são {alunos[flag][1]} {alunos[flag][2]}')

print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')
