# Escreva um programa que leia dois números inteiro e compare-os mostrando na tela uma mensagem:


n1 = int(input('Primeiro número: '))
n2 = int(input('Segunod  número: '))


if n2 > n1:
    print('O SEGUNDO número é maior')
elif n1 == n2:
    print('Os dois valores são IGUAIS')
else:
    print('O PRIMEIRO valor é maior')
