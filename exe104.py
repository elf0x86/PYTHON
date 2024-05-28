# Crie um programa que tenha a função leia_int(), que vai funcionar de forma semelhante á função input()
# só que fazendo a validação para aceitar apenas um valor numérico
# Ex: n = leia_int('Digite um numero: ')


def leia_int(msg):
    valor = input(msg)

    while not (valor.isdigit()):
        print('\033[1;31mErro! Digite um número inteiro valido\033[m')
        valor = input(msg)

    return valor

n = leia_int("Qual seu número favorito? ")
print(f'O valor de n --> {n}')


# SOLUÇÃO DO VIDEO ----------------------------------------------------------------------------
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

# Programa principal
N = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {N}')
