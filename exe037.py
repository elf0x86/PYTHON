# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolha qual será a base de conversão

numero = int(input('Digite um número inteiro: '))
escolha = int(input('''Escolha um adas bases para conversão
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opção: '''))

if escolha == 1:
    print(f'{numero} para HEXADECIMAL {hex(numero)}')
elif escolha == 2:
    print(f'{numero} para OCTAL {oct(numero)}')
elif escolha == 3:
    print(f'{numero} para EXADECIMAL {hex(numero)}')
else:
    print(f'Algo de Errado.')


