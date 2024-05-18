# Crie um programa que leia vários números inteiros pelo teclado.
# O programa sé vai para quando o usuário digitar o valor 999, que é a condição de parada
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# desconsiderando a flag


flag = int(input("Digite um número de 0 a 998: "))
soma = 0

while flag != 999:
    soma += flag
    flag = int(input("Digite um número de 0 a 998: "))

print(f'A soma é {soma}')

# Solução do video ----------------------------------------------------------------------
num  = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um numero [999 para parar]: '))
    soma += num
    cont += 1

print(f'Você digitou {cont - 1} números. E a soma entre eles foi {soma - 999}')

