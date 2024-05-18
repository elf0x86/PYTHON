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


