# Crie um programa que tenha a função leia_int(), que vai funcionar de forma semelhante á função input()
# só que fazendo a validação para aceitar apenas um valor numérico
# Ex: n = leia_int('Digite um numero: ')


def leia_int(msg):
    while True:
        try:
            valor = int(input(msg))
        except ValueError as eRRo:
            print(f'\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            return valor
        finally:
           print('Certo ou Errado o importante é tentar!')


def leia_float(msg):
    while True:
        try:
            valor = float(input(msg))
        except ValueError as eRRo:
            print(f'\033[1;31mERRO: por favor, digite um número decimal válido.\033[m')
        else:
            return valor
        finally:
           print('\033[1;32mCerto ou Errado o importante é tentar!\033[m')


n = leia_int("Qual seu número INTEIRO favorito? ")
print(f'O valor de n --> {n}')

m = leia_float("Qual seu número DECIMAL favorito? ")
print(f'O valor de m --> {m}')


