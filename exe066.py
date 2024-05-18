# Crie um programa que leia vários números inteiros pelo teclado. O programa
# só vai parar quando o usuário digitar o valor 999, que é a condição de
# parada. No fina mostre quantos números foram digitados e qual foi a soma
# entre eles (desconsiderando a flag)

total = 0
soma  = 0

while True:
    buffer = float(input('Entre com um número [999] para SAIR: '))
    if buffer == 999:
        break
    else:
        soma += buffer
    total += 1

print(f'Ao todo foram digitador {total} numeros. A soma entre todos é de {soma}')
