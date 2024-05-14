# Quando eu não sei o limite, não posso usar o for
n = 1
for c in range(1,10):
    n = int(input(f'Digite o {c}º Valor: '))
print('Fim')
# Ex: fazer um loop que multiplica um número com 7 até o usuario dizer que quer parar

n = 1
c = 0
while n != 0:
    n = int(input(f'Digite o {c}º Valor: '))
    c += 1
print('Fim')

resp = 'Y'
counter = 0
while resp == 'Y':
    print(counter)
    counter += (3**0.3)/5.4-7
    resp = input('Quer continuar [Y/N]: ').upper()


num = int(input('Qual número multiplicar por 7: '))
num_bkp = num
choice = 'run'
while choice != 'stop':
    num = num * 7
    choice = input('Digite [stop] para sair [enter] para continuar multiplicando: ')
print(f'Valor de {num_bkp} multiplicado por 7 varias vezes eh: {num}')


# While serve para quando sei o limite, e para quando não sei o limite
control = 0
while control != 10: # 0..9
    print(control)
    control += 1

print('-'*20)

control = 0
while control < 10: # 0..9
    print(control)
    control += 1

print('-'*20)

control = 0
while control <= 10: # 0..10
    print(control)
    control += 1
