# faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
# escrever na tela se o usuário venceu ou perdeu.
from random import randint


print('--' + '=--'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('--' + '=--'*20)

numero = randint(0,5)
chute = int(input("Em que número em pensei? "))

if chute == numero:
    print('Parabéns você ganhou!')
else:
    print(f'Você errou. o número que eu pensei foi {numero}.')
~                                                                 
