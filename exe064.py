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
print(soma) # ainda tem 999 somado junto as opçoes
soma = soma - 999 # sulução para o proplema tirar 999 da soma apos o loop
print(soma) # valor desejado 

# Solução 2 do video  ----------------------------------------------------------------------
num  = 0
cont = 0
soma = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para parar]: '))

print(f'Você digitou {cont} números. E a soma entre eles foi {soma}')


