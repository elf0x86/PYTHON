# Crie um programa que faça o computador jogar jokenpo com você

from random import randint
from os import system

computer_choice = randint(0,2)
user_choice     = int(input('''Suas opçẽos
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é sua jogada? '''))

choices = 'PEDRA PAPEL TESOURA'

print('JO')
system('sleep 0.5')
print('KEN')
system('sleep 0.5')
print('PO!!!')
system('sleep 0.5')

print('-=' * 20)
if computer_choice == 0 and user_choice == 2:
    print(f'Computador Jogou PEDRA')
    print(f'Você Jogou TESOURA')
    print('-=' * 20)
    print(f'COMPUTADOR VENCEU')
elif computer_choice == 1 and user_choice == 0:
    print(f'Computador Jogou TESOURA')
    print(f'Você Jogou PEDRA')
    print('-=' * 20)
    print(f'COMPUTADOR VENCEU')
elif computer_choice == 2 and user_choice == 1:
    print(f'Computador Jogou TESOURA')
    print(f'Você Jogou PAPEL')
    print('-=' * 20)
    print(f'COMPUTADOR VENCEU')
elif computer_choice == user_choice:
    print('É UM EMPATE')
    print('-=' * 20)
else:
    print(f'Computador Jogou {choices.split()[computer_choice]}')
    print(f'Você Jogou {choices.split()[user_choice]}')
    print('-=' * 20)
    print(f"VOCÊ VENCEU")


