# Crie um programa que tenha uma função fatorial() que receba dois parametros:
# O primeiro que indique o número a calcular
# O segundo chamado show, que será um valor lógico (opcional)
# indicando se será mastrado ou não na tela o processo de cálculo do fatorial


def fatorial_v0(n=1, show=False):
    '''
    :param n: recebe um valor inteiro para calcular o fatorial. O valor padrão é 1
    :param show: mostra o fatorial sendo construido com um delay de 0.3 segundos de linha em linha
    '''
    from time import sleep
    tmp = 0
    if show == True:
        for x in range(n, 0, -1):
            if x == n:
                tmp = x
                sleep(0.3)
                print(x, end=' ', flush=True)
            elif x < tmp:
                sleep(0.3)
                tmp = tmp * x
                print(x, end=' ', flush=True)
            sleep(0.3)
            print(f'-> {tmp}', flush=True)
    else:
        for x in range(n, 0, -1):
            if x == n:
                tmp = x
            elif x < tmp:
                tmp = tmp * x
        print(f'{tmp}', flush=True)



def fatorial_v1(n=1, show=False):
    '''
    :param n: recebe um valor inteiro para calcular o fatorial. O valor padrão é 1
    :param show: mostra o fatorial sendo construido com um delay de 0.3 segundos em uma linha
    '''
    from time import sleep
    tmp = 0
    if show == True:
        for x in range(n, 0, -1):
            if x == n:
                tmp = x
                sleep(0.3)
                print(x, end=' ', flush=True)
            elif x < tmp:
                tmp = tmp * x
                sleep(0.3)
                print(x, end=' ', flush=True)
        sleep(0.3)
        print(f'= {tmp}', flush=True)
    else:
        for x in range(n, 0, -1):
            if x == n:
                tmp = x
            elif x < tmp:
                tmp = tmp * x
        print(f'{tmp}')


fatorial_v0()
fatorial_v0(5)
fatorial_v0(5, show=True)

print('=' * 40)

fatorial_v1()
fatorial_v1(5)
fatorial_v1(5, show=True)

help(fatorial_v0)
help(fatorial_v1)


# SOLUÇÃO DO VIDEO ------------------------------------------------------------------------------

def fatorial(n, show=False):
    '''
    CALCULA O FATORIAL DE UM NÚMERO
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor fanoria de um número n
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(5, show=True))
help(fatorial)
