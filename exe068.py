# Faça um programa que jogue par ou limpar com o computador. O jogo só será interrompido 
# quando o jogador PERDER, mostrando o total de vitórios consecutivas que ele conquistou
# no final do jogo.

import random

user_wins      = 0
computer_wins  = 0

while True:
    computer_number_choice = random.randint(0, 10) # ten is inclusive
    user_number_choice     = int(input('Entre com um número de 0-10: '))
    user_option_choice     = input('[ P ] Para escolher PAR\n[ I ] Para escolher IMPAR\n.:').strip().upper()[0]

    if user_number_choice > 11:
        print('Numero invalido. TENTE NOVAMENTE')
    else:
        if (computer_number_choice + user_number_choice) % 2 == 0 and user_option_choice == 'P':
            user_wins += 1
            print('Voce ganhou com PAR')
        elif (computer_number_choice + user_number_choice) % 2 != 0 and user_option_choice == 'I':
            user_wins += 1
            print('Voce ganhou com IMPAR')
        else:
            #computer_wins += 1
            break

print(f'Vitorias consecutivas {user_wins}')

# Solução do video ------------------------------------------------------------------
from random import randint
vitoria = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar [P/I]? ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU')
            vitoria += 1
        else:
            print('Voce PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU')
            vitoria += 1
        else:
            print('Voce PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vezes.')
