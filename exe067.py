# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
# digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo


while True:
    n = int(input('Digite um número para ver a tabuada: '))
    if n < 0:
        break
    else:
        for x in range(0, 11):
            print(f'{x: >2} x {n} = {x*n: >2}')


