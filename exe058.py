from random import randint


print('--' + '=--'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('--' + '=--'*20)

numero     = randint(0,5)
chute      = int(input("Em que número eu pensei? "))
tentativas = 1

while chute != numero:

    if chute == numero:
        print('Parabéns você acertou!')
    else:
        print(f'Você errou! Tente NOVAMENTE')

    chute = int(input("Em que número eu pensei? "))
    tentativas += 1

print(f'Você jogou {tentativas} vezes para acertar o número que eu pensei!')


# Solução do video
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {palpites} tentativas. Parabéns!')
