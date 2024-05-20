# Crie um porgrama que tenha uma tupla totalmente preenchida com uma contagem
# por extenso, de zero até vinte. Seu programa deverá ler um número pelo
# teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem_extenso = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
                    'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
                    'quinze', 'deseseis', 'desesete', 'dezoito', 'dezenove',
                    'vinte')

while True:
    numero = int(input('Digite um número de 0 a 20: '))
    if numero <= 20:
        print(f'Você digitou o número \033[1;32m{contagem_extenso[numero]}\033[m')
    else:
        print('\033[1;33mNUMERO INVALIDO TENTE NOVAMENTE!\033[m')

    flag = input('Quer continuar [S/N]: ').strip().upper()[0]
    if flag == 'N':
        break
    else:
        continue

# Solução do video ----------------------------------------------------------
cont = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
                    'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
                    'quinze', 'deseseis', 'desesete', 'dezoito', 'dezenove',
                    'vinte')

while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20: # if you type 20 will raise an error index out of range 
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}')
