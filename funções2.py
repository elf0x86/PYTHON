# DOCSTRINGS

# QUE SIGNIFICA i,f,p PARA QUEM DEFINE A FUNÇÃO PARECE FACIL. 
# MAS PARA QUEM FOR USAR A FUNÇÃO ?
# COMO VAI SABER O QUE i,f,p SIGNIFICA ?                                           
                     
def contador(i,f,p): 
    '''
    -> Faz uma contagem e mostra na tela.
    :parametro (i): Inicio da contagem
    :parametro (f): fim da contagem
    :parametro (p): passo da contagem
    :retrun       : sem retorno
    Função criada por SAM 28/05/2024
    '''
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM.')


def somar(a=0, b=0, c=0): # default parrameters
    '''
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a=0: o primeiro valor
    :param b=0: o segundo valor
    :param c=0: o terceiro valor
    A parameter is the variable listed inside the parentheses in the function definition. 
    An argument is the value that are sent to the function when it is called.
    '''
    s = a + b + c
    print(f'A soma vale {s}')


#help(contador)
contador(2, 10, 2)

#help(somar)
somar()
somar(c=2, b=3) # not in order optional argumets

print('=' * 30)


# ESCOPO GLOBAL DE VARIÁVEIS
def test():
    print(f'Na função teste, n vale {n}')
    

# PROGRMA PRINCIPAL
n = 2
print(f'No programa principal, n vale {n}')
test()



print('=' * 30)

# ESCOPO LOCAL DE VARIÁVEIS
def test1():
    x = 8  # x tem um escopo local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}') 

# PROGRMA PRINCIPAL
n = 2
print(f'No programa principal, n vale {n}')
# print(f'No programa principal, x vale {x}') # RETORNA UM ERRO DIZENDO QUE {X} NÃO FOI DEFINIDO
test1()



print('=' * 30)

def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')


print('=' * 30)


def teste(b):
    global a
    a = 777
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
print(f'A fora vale {a}')
print('-' * 30)
teste(a)
print('-' * 30)
print(f'A fora vale {a}')

print('=' * 30)

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3,2,5)
r2 = somar(2, 5)
r3 = somar(8)

print(f'Os resultados foram {r1}, {r2} e {r3}.')
