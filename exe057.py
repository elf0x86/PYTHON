# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'
# Caso estra errado, peça o a digitação novamente até ter um valor correto


sexo = ''
while not ('M' in sexo or 'F' in sexo):
    sexo = input('Qual sexo do cidadão [M/F]? ')
    if not sexo in 'MF':
        print('\033[1;31mOPÇÃO INVALIDA tente novamente!\033[m')


# Solução do VIDEO
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos por favor informe seu sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
